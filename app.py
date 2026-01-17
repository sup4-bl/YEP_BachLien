# app.py - Main Flask Application with Back Navigation - FIXED VERSION
from flask import Flask, render_template, request, session, redirect, url_for, g
import secrets
import qrcode
from io import BytesIO
import base64
import os
import sqlite3
from datetime import datetime

from config import (
    ADMIN_PASSWORD, DB_PATH, NHAN_VIEN, 
    TIET_MUC_OPTIONS, TIET_MUC_IMAGES, TIET_MUC_SET,
    KINGS_PHONG_BAN, QUEENS_PHONG_BAN,
    get_forbidden_tiet_muc_for_department
)

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# =========================
# DATABASE FUNCTIONS
# =========================
def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH, check_same_thread=False)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(_exc):
    db = g.pop("db", None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    db.execute("""
        CREATE TABLE IF NOT EXISTS votes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            vote_type TEXT NOT NULL,
            vote_value TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT (datetime('now'))
        );
    """)
    db.execute("""
        CREATE TABLE IF NOT EXISTS voted_users (
            username TEXT PRIMARY KEY,
            voted_at TEXT NOT NULL DEFAULT (datetime('now'))
        );
    """)
    db.execute("CREATE INDEX IF NOT EXISTS idx_votes_type ON votes(vote_type);")
    db.execute("CREATE INDEX IF NOT EXISTS idx_votes_user ON votes(username);")
    db.execute("CREATE UNIQUE INDEX IF NOT EXISTS uq_vote_once_value ON votes(username, vote_type, vote_value);")
    db.commit()

def user_has_voted(username: str) -> bool:
    db = get_db()
    row = db.execute("SELECT 1 FROM voted_users WHERE username = ? LIMIT 1", (username,)).fetchone()
    return row is not None

def mark_user_voted(username: str):
    db = get_db()
    db.execute("INSERT OR REPLACE INTO voted_users(username, voted_at) VALUES(?, datetime('now'))", (username,))
    db.commit()

def insert_vote(username: str, vote_type: str, vote_value: str):
    db = get_db()
    db.execute(
        "INSERT OR IGNORE INTO votes(username, vote_type, vote_value, created_at) VALUES(?, ?, ?, datetime('now'))",
        (username, vote_type, vote_value),
    )

def save_tiet_muc_votes(username: str, selected_depts: list):
    db = get_db()
    db.execute("BEGIN")
    db.execute("DELETE FROM votes WHERE username = ? AND vote_type = 'tiet_muc'", (username,))
    for dept in selected_depts:
        insert_vote(username, "tiet_muc", dept)
    db.commit()

def save_single_vote(username: str, vote_type: str, vote_value: str):
    db = get_db()
    db.execute("BEGIN")
    db.execute("DELETE FROM votes WHERE username = ? AND vote_type = ?", (username, vote_type))
    insert_vote(username, vote_type, vote_value)
    db.commit()

def get_user_votes(username: str, vote_type: str) -> list:
    """Get existing votes for a user and vote type"""
    db = get_db()
    rows = db.execute(
        "SELECT vote_value FROM votes WHERE username = ? AND vote_type = ?",
        (username, vote_type)
    ).fetchall()
    return [row["vote_value"] for row in rows]

def get_user_progress(username: str) -> dict:
    """Return persisted progress for a user based on existing votes."""
    db = get_db()

    # Exactly 3 items are required for 'tiet_muc'
    tiet_muc_cnt = db.execute(
        "SELECT COUNT(1) AS c FROM votes WHERE username = ? AND vote_type = 'tiet_muc'",
        (username,),
    ).fetchone()["c"]
    king_cnt = db.execute(
        "SELECT COUNT(1) AS c FROM votes WHERE username = ? AND vote_type = 'king'",
        (username,),
    ).fetchone()["c"]
    queen_cnt = db.execute(
        "SELECT COUNT(1) AS c FROM votes WHERE username = ? AND vote_type = 'queen'",
        (username,),
    ).fetchone()["c"]

    return {
        "tiet_muc_done": int(tiet_muc_cnt) == 3,
        "king_done": int(king_cnt) >= 1,
        "queen_done": int(queen_cnt) >= 1,
    }

# =========================
# HELPER FUNCTIONS
# =========================
def generate_qr_png_data_uri(data: str) -> str:
    """Generate QR as PNG data URI."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    bio = BytesIO()
    img.save(bio, format="PNG")
    b64 = base64.b64encode(bio.getvalue()).decode("utf-8")
    return f"data:image/png;base64,{b64}"


def _get_person_photo_url(username: str, default_svg_url: str) -> str:
    """
    Return photo URL if exists in static/img/people, otherwise default avatar SVG.
    
    FIX: This version doesn't check file existence on server.
    Instead, it always returns the expected path and lets the browser handle
    the fallback via onerror attribute in the HTML template.
    """
    # List of possible extensions in priority order
    extensions = [".jpg", ".jpeg", ".png", ".webp"]
    
    # Check in-memory cache first (optional optimization)
    cache_key = f"photo_{username}"
    if hasattr(app, '_photo_cache') and cache_key in app._photo_cache:
        return app._photo_cache[cache_key]
    
    # Try to find the file
    base_path = os.path.join(app.root_path, "static", "img", "people")
    
    # Create cache if not exists
    if not hasattr(app, '_photo_cache'):
        app._photo_cache = {}
    
    # Check if directory exists
    if os.path.exists(base_path):
        for ext in extensions:
            filename = username + ext
            full_path = os.path.join(base_path, filename)
            if os.path.exists(full_path):
                photo_url = f"/static/img/people/{filename}"
                app._photo_cache[cache_key] = photo_url
                return photo_url
    
    # If not found locally, still try the URL path
    # The onerror in template will handle missing files
    for ext in extensions:
        photo_url = f"/static/img/people/{username}{ext}"
        # Don't cache the default, in case file is added later
        return photo_url
    
    # Fallback to default avatar
    return default_svg_url

def dense_rank(items):
    """Dense ranking with ties"""
    rank = 0
    prev_votes = None
    out = []
    for it in items:
        v = it["votes"]
        if prev_votes is None:
            rank = 1
        elif v < prev_votes:
            rank += 1
        it2 = dict(it)
        it2["rank"] = rank
        out.append(it2)
        prev_votes = v
    return out

def query_results_tiet_muc():
    db = get_db()
    rows = db.execute("""
        SELECT vote_value AS dept, COUNT(*) AS cnt
        FROM votes
        WHERE vote_type = 'tiet_muc'
        GROUP BY vote_value
        ORDER BY cnt DESC, vote_value ASC
    """).fetchall()
    items = [{"name": r["dept"], "department": None, "votes": int(r["cnt"])} for r in rows]
    return dense_rank(items)

def query_results_people(vote_type: str):
    db = get_db()
    rows = db.execute("""
        SELECT vote_value AS emp_username, COUNT(*) AS cnt
        FROM votes
        WHERE vote_type = ?
        GROUP BY vote_value
        ORDER BY cnt DESC, vote_value ASC
    """, (vote_type,)).fetchall()
    
    items = []
    for r in rows:
        u = r["emp_username"]
        if u in NHAN_VIEN:
            items.append({
                "name": f"{NHAN_VIEN[u]['name']} ({u})",
                "department": NHAN_VIEN[u]["department"],
                "votes": int(r["cnt"]),
            })
        else:
            items.append({"name": f"(Unknown) ({u})", "department": None, "votes": int(r["cnt"])})
    return dense_rank(items)

# =========================
# MAIN ROUTES
# =========================
@app.before_request
def _ensure_db():
    init_db()

@app.route("/", methods=["GET", "POST"])
def login():
    qr_code = generate_qr_png_data_uri(request.host_url)
    
    if request.method == "POST":
        username = request.form.get("username", "").strip().lower()
        
        if username not in NHAN_VIEN:
            return render_template("login.html", error="Tài khoản không tồn tại!", qr_code=qr_code)
        
        # Check if user has COMPLETED voting (marked as voted)
        if user_has_voted(username):
            return render_template("login.html", error="Bạn đã bình chọn rồi!", qr_code=qr_code)
        
        session.clear()
        session["username"] = username
        session["name"] = NHAN_VIEN[username]["name"]
        session["department"] = NHAN_VIEN[username]["department"]

        # Restore progress so the user can continue where they left off
        progress = get_user_progress(username)
        session["tiet_muc_done"] = bool(progress.get("tiet_muc_done"))
        session["king_done"] = bool(progress.get("king_done"))
        session["queen_done"] = bool(progress.get("queen_done"))

        if not session["tiet_muc_done"]:
            return redirect(url_for("vote_tiet_muc"))
        if not session["king_done"]:
            return redirect(url_for("vote_king"))
        if not session["queen_done"]:
            return redirect(url_for("vote_queen"))
        # Fallback
        return redirect(url_for("vote_tiet_muc"))
    
    return render_template("login.html", error=None, qr_code=qr_code)

@app.route("/vote/tiet-muc", methods=["GET", "POST"])
def vote_tiet_muc():
    if "username" not in session:
        return redirect(url_for("login"))

    # Block if already completed all voting
    if user_has_voted(session["username"]):
        return redirect(url_for("login"))

    error = None
    user_dept = session["department"]
    forbidden = get_forbidden_tiet_muc_for_department(user_dept)
    visible_options = [opt for opt in TIET_MUC_OPTIONS if opt not in forbidden]

    # Load existing votes from database
    existing_votes = get_user_votes(session["username"], "tiet_muc")

    if request.method == "POST":
        votes = request.form.getlist("votes")
        
        if len(votes) != 3:
            error = "Bạn phải chọn đúng 3 tiết mục."
        else:
            invalid = [v for v in votes if v not in TIET_MUC_SET or v in forbidden]
            if invalid:
                error = "Có tiết mục không hợp lệ hoặc bạn không được vote."
            else:
                save_tiet_muc_votes(session["username"], votes)
                session["tiet_muc_done"] = True
                return redirect(url_for("vote_king"))

    return render_template(
        "vote_tiet_muc.html",
        name=session["name"],
        department=user_dept,
        departments=visible_options,
        forbidden_options=forbidden,
        images=TIET_MUC_IMAGES,
        existing_votes=existing_votes,
        error=error,
    )

@app.route("/vote/king", methods=["GET", "POST"])
def vote_king():
    if "username" not in session:
        return redirect(url_for("login"))

    # Block if already completed
    if user_has_voted(session["username"]):
        return redirect(url_for("login"))

    progress = get_user_progress(session["username"])
    # Require that 'tiet_muc' is completed (persisted)
    if not progress.get("tiet_muc_done"):
        return redirect(url_for("vote_tiet_muc"))
    session["tiet_muc_done"] = True
    
    error = None
    other_depts = {k: v for k, v in KINGS_PHONG_BAN.items() if k != session["department"]}
    default_avatar = "/static/img/avatars/male.svg"
    departments = {
        dept: [
            {
                **emp,
                "photo": _get_person_photo_url(emp["username"], default_avatar),
                "fallback": default_avatar,
            }
            for emp in emps
        ]
        for dept, emps in other_depts.items()
    }
    
    # Load existing vote
    existing_vote = get_user_votes(session["username"], "king")
    selected_username = existing_vote[0] if existing_vote else None
    
    if request.method == "POST":
        vote_username = (request.form.get("vote") or "").strip().lower()
        
        if not vote_username:
            error = "Bạn phải chọn 1 người để tiếp tục."
        elif vote_username not in NHAN_VIEN:
            error = "Lựa chọn không hợp lệ."
        elif NHAN_VIEN[vote_username]["department"] == session["department"]:
            error = "Bạn không thể vote cho người thuộc phòng ban của mình."
        else:
            save_single_vote(session["username"], "king", vote_username)
            session["king_done"] = True
            return redirect(url_for("vote_queen"))
    
    return render_template(
        "vote_king.html",
        name=session["name"],
        department=session["department"],
        departments=departments,
        selected_username=selected_username,
        can_go_back=True,
        error=error,
    )

@app.route("/vote/queen", methods=["GET", "POST"])
def vote_queen():
    if "username" not in session:
        return redirect(url_for("login"))

    # Block if already completed
    if user_has_voted(session["username"]):
        return redirect(url_for("login"))

    progress = get_user_progress(session["username"])
    if not progress.get("king_done"):
        return redirect(url_for("vote_king"))
    session["tiet_muc_done"] = True
    session["king_done"] = True
    
    error = None
    other_depts = {k: v for k, v in QUEENS_PHONG_BAN.items() if k != session["department"]}
    default_avatar = "/static/img/avatars/female.svg"
    departments = {
        dept: [
            {
                **emp,
                "photo": _get_person_photo_url(emp["username"], default_avatar),
                "fallback": default_avatar,
            }
            for emp in emps
        ]
        for dept, emps in other_depts.items()
    }
    
    # Load existing vote
    existing_vote = get_user_votes(session["username"], "queen")
    selected_username = existing_vote[0] if existing_vote else None
    
    if request.method == "POST":
        vote_username = (request.form.get("vote") or "").strip().lower()
        
        if not vote_username:
            error = "Bạn phải chọn 1 người để hoàn thành."
        elif vote_username not in NHAN_VIEN:
            error = "Lựa chọn không hợp lệ."
        elif NHAN_VIEN[vote_username]["department"] == session["department"]:
            error = "Bạn không thể vote cho người thuộc phòng ban của mình."
        else:
            save_single_vote(session["username"], "queen", vote_username)
            session["queen_done"] = True
            mark_user_voted(session["username"])  # FINALIZE voting
            return redirect(url_for("thank_you"))
    
    return render_template(
        "vote_queen.html",
        name=session["name"],
        department=session["department"],
        departments=departments,
        selected_username=selected_username,
        can_go_back=True,
        error=error,
    )

@app.route("/vote/back-to-tiet-muc")
def back_to_tiet_muc():
    if "username" not in session:
        return redirect(url_for("login"))
    
    # Block if already completed
    if user_has_voted(session["username"]):
        return redirect(url_for("login"))
    
    # Reset progress flags to allow editing
    session["king_done"] = False
    session["queen_done"] = False
    return redirect(url_for("vote_tiet_muc"))

@app.route("/vote/back-to-king")
def back_to_king():
    if "username" not in session:
        return redirect(url_for("login"))
    
    # Block if already completed
    if user_has_voted(session["username"]):
        return redirect(url_for("login"))
    
    # Reset queen flag
    session["queen_done"] = False
    return redirect(url_for("vote_king"))

@app.route("/thank-you")
def thank_you():
    if not session.get("queen_done"):
        return redirect(url_for("login"))
    name = session.get("name", "Bạn")
    session.clear()
    return render_template("thank_you.html", name=name)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# =========================
# ADMIN ROUTES
# =========================
@app.route("/admin", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        password = request.form.get("password", "")
        if password == ADMIN_PASSWORD:
            session["admin"] = True
            return redirect(url_for("admin_menu"))
        return render_template("admin_login.html", error="Mật khẩu không đúng!")
    return render_template("admin_login.html", error=None)

@app.route("/admin/menu")
def admin_menu():
    if not session.get("admin"):
        return redirect(url_for("admin_login"))
    return render_template("admin_menu.html")

@app.route("/admin/results/tiet-muc")
def admin_results_tiet_muc():
    if not session.get("admin"):
        return redirect(url_for("admin_login"))
    
    ranked = query_results_tiet_muc()
    max_votes = max([it["votes"] for it in ranked], default=0)

    return render_template(
        "admin_results.html",
        title="Tiết Mục Yêu Thích",
        icon="🎭",
        results=ranked,
        max_votes=max_votes,
        has_any=(len(ranked) > 0),
        show_department=False,
        page_type="tiet_muc"
    )

@app.route("/admin/results/king")
def admin_results_king():
    if not session.get("admin"):
        return redirect(url_for("admin_login"))
    
    ranked = query_results_people("king")
    max_votes = max([it["votes"] for it in ranked], default=0)

    return render_template(
        "admin_results.html",
        title="King",
        icon="👑",
        results=ranked,
        max_votes=max_votes,
        has_any=(len(ranked) > 0),
        show_department=True
    )

@app.route("/admin/results/queen")
def admin_results_queen():
    if not session.get("admin"):
        return redirect(url_for("admin_login"))
    
    ranked = query_results_people("queen")
    max_votes = max([it["votes"] for it in ranked], default=0)

    return render_template(
        "admin_results.html",
        title="Queen",
        icon="👸",
        results=ranked,
        max_votes=max_votes,
        has_any=(len(ranked) > 0),
        show_department=True
    )

@app.route("/admin/logout")
def admin_logout():
    session.pop("admin", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    with app.app_context():
        init_db()
    app.run(debug=True, host="0.0.0.0", port=5000)