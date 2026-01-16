# config.py - Configuration và Data
import os

# Admin Password
ADMIN_PASSWORD = "admin123"

# Database Path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "yep_voting.db")

# Dữ liệu nhân viên
NHAN_VIEN = {
    # ===== QUEENS - NHÂN VIÊN NỮ (88 người) =====
    "nv013": {"password": "123", "name": "Đàm Thị Thanh Vân", "department": "KINH DOANH 1"},
    "nv014": {"password": "123", "name": "Nguyễn Thị Lan Anh", "department": "XUẤT NHẬP KHẨU"},
    "nv016": {"password": "123", "name": "Trần Hoa Lý", "department": "MUA HÀNG"},
    "nv017": {"password": "123", "name": "Trần Thị Thương Huyền", "department": "BAN GIÁM ĐỐC"},
    "nv021": {"password": "123", "name": "Nguyễn Thị Ngọc Mai", "department": "KINH DOANH 2"},
    "nv025": {"password": "123", "name": "Vũ Thị Thanh Thủy", "department": "KINH DOANH 4"},
    "nv026": {"password": "123", "name": "Đỗ Thị Mai Phương", "department": "KINH DOANH 2"},
    "nv032": {"password": "123", "name": "Nguyễn Kim Phượng", "department": "KẾ TOÁN"},
    "nv033": {"password": "123", "name": "Trần Thị Thu Phương", "department": "XUẤT NHẬP KHẨU"},
    "nv036": {"password": "123", "name": "Nguyễn Thị Kim Dung", "department": "HÀNH CHÍNH - NHÂN SỰ"},
    "nv052": {"password": "123", "name": "Nguyễn Thị Hà", "department": "MUA HÀNG"},
    "nv053": {"password": "123", "name": "Phạm Thị Thu Hoài", "department": "MUA HÀNG"},
    "nv055": {"password": "123", "name": "Đinh Quỳnh Hương", "department": "KINH DOANH 2"},
    "nv056": {"password": "123", "name": "Đặng Thùy Linh", "department": "CÔNG NGHỆ"},
    "nv058": {"password": "123", "name": "Triệu Thị Nhung", "department": "HÀNH CHÍNH - NHÂN SỰ"},
    "nv059": {"password": "123", "name": "Nguyễn Hải Chi", "department": "KINH DOANH 3"},
    "nv064": {"password": "123", "name": "Vũ Thúy Hằng", "department": "XUẤT NHẬP KHẨU"},
    "nv071": {"password": "123", "name": "Phạm Thị Mạnh Quỳnh", "department": "KINH DOANH 2"},
    "nv072": {"password": "123", "name": "Phùng Thị Kim Ngân", "department": "KHO VẬN"},
    "nv084": {"password": "123", "name": "Trần Thùy Linh", "department": "KINH DOANH 3"},
    "nv087": {"password": "123", "name": "Nguyễn Thị Thu Uyên", "department": "MUA HÀNG"},
    "nv089": {"password": "123", "name": "Trần Thị Ngọc Mai", "department": "XUẤT NHẬP KHẨU"},
    "nv090": {"password": "123", "name": "Nguyễn Thu Lan", "department": "KINH DOANH 2"},
    "nv094": {"password": "123", "name": "Trần Hương Giang", "department": "MUA HÀNG"},
    "nv096": {"password": "123", "name": "Lê Thị Mai Thúy", "department": "KẾ TOÁN"},
    "nv097": {"password": "123", "name": "Ngô Thị Phụng", "department": "MUA HÀNG"},
    "nv098": {"password": "123", "name": "Trịnh Thu Uyên", "department": "KINH DOANH 2"},
    "nv102": {"password": "123", "name": "Đỗ Hoài Phương", "department": "KHO VẬN"},
    "nv108": {"password": "123", "name": "Vũ Thị Hồng Nhung", "department": "CÔNG NGHỆ"},
    "nv110": {"password": "123", "name": "Nguyễn Thị Kim Anh", "department": "XUẤT NHẬP KHẨU"},
    "nv117": {"password": "123", "name": "Lê Thị Cẩm Ly", "department": "KINH DOANH 3"},
    "nv119": {"password": "123", "name": "Mai Thị Thu Huyền", "department": "KINH DOANH 3"},
    "nv127": {"password": "123", "name": "Phạm Thị Thu Hằng", "department": "KHO VẬN"},
    "nv128": {"password": "123", "name": "Bùi Khánh Linh", "department": "KINH DOANH 3"},
    "nv134": {"password": "123", "name": "Phạm Thị Chữ", "department": "HÀNH CHÍNH - NHÂN SỰ"},
    "nv139": {"password": "123", "name": "Phan Ngân Hà", "department": "KINH DOANH 4"},
    "nv146": {"password": "123", "name": "Phạm Thị Nhung", "department": "HÀNH CHÍNH - NHÂN SỰ"},
    "nv149": {"password": "123", "name": "Đỗ Thị Ngát", "department": "KẾ TOÁN"},
    "nv151": {"password": "123", "name": "Hoàng Thị Hằng", "department": "KẾ TOÁN"},
    "nv152": {"password": "123", "name": "Trần Thị Thanh Hằng", "department": "CÔNG NGHỆ"},
    "nv156": {"password": "123", "name": "Đỗ Thu Thảo", "department": "KẾ TOÁN"},
    "nv161": {"password": "123", "name": "Hồ Thị Thúy Hiền", "department": "KẾ TOÁN"},
    "nv169": {"password": "123", "name": "Nông Hồng Nhung", "department": "KINH DOANH 1"},
    "nv171": {"password": "123", "name": "Đỗ Thùy Linh", "department": "KINH DOANH 2"},
    "nv173": {"password": "123", "name": "Trần Linh Chi", "department": "KINH DOANH 1"},
    "nv178": {"password": "123", "name": "Trần Thị Thúy Quỳnh", "department": "KINH DOANH 2"},
    "nv179": {"password": "123", "name": "Nguyễn Thị Vân Anh", "department": "XUẤT NHẬP KHẨU"},
    "nv182": {"password": "123", "name": "Vũ Ngọc Linh", "department": "KINH DOANH 1"},
    "nv185": {"password": "123", "name": "Nguyễn Thị Hương Giang", "department": "KINH DOANH 2"},
    "nv189": {"password": "123", "name": "Lưu Thị Tú Anh", "department": "KINH DOANH 2"},
    "nv190": {"password": "123", "name": "Nguyễn Huyền Trang", "department": "KINH DOANH 2"},
    "nv191": {"password": "123", "name": "Đặng Thị Thu", "department": "KINH DOANH 3"},
    "nv193": {"password": "123", "name": "Nguyễn Thị Thúy", "department": "KẾ TOÁN"},
    "nv195": {"password": "123", "name": "Nguyễn Thùy Linh", "department": "KINH DOANH 3"},
    "nv198": {"password": "123", "name": "Trần Huyền Anh", "department": "KINH DOANH 3"},
    "nv206": {"password": "123", "name": "Chu Thanh Huyền", "department": "KINH DOANH 2"},
    "nv211": {"password": "123", "name": "Ngụy Thị Thu Hằng", "department": "KINH DOANH 3"},
    "nv213": {"password": "123", "name": "Lê Thị Ngân", "department": "KINH DOANH 2"},
    "nv216": {"password": "123", "name": "Nguyễn Thúy Hằng", "department": "KINH DOANH 2"},
    "nv218": {"password": "123", "name": "Nguyễn Thị Thu Hà", "department": "KINH DOANH 2"},
    "nv219": {"password": "123", "name": "Lê Minh Thúy", "department": "KINH DOANH 2"},
    "nv222": {"password": "123", "name": "Nguyễn Thanh Hương", "department": "KINH DOANH 2"},
    "nv223": {"password": "123", "name": "Lưu Thị Thu Hiền", "department": "MUA HÀNG"},
    "nv238": {"password": "123", "name": "Đỗ Mai Linh", "department": "KẾ TOÁN"},
    "nv240": {"password": "123", "name": "Đỗ Quỳnh Chi", "department": "KẾ TOÁN"},
    "nv242": {"password": "123", "name": "Lê Ngọc Ánh", "department": "KINH DOANH 2"},
    "nv243": {"password": "123", "name": "Lê Yến Nhi", "department": "HÀNH CHÍNH - NHÂN SỰ"},
    "nv244": {"password": "123", "name": "Nguyễn Khắc Thiên Trang", "department": "KINH DOANH 4"},
    "nv245": {"password": "123", "name": "Nguyễn Minh Ánh", "department": "KINH DOANH 1"},
    "nv252": {"password": "123", "name": "Vũ Thị Huyền Trang", "department": "CÔNG NGHỆ"},
    "nv255": {"password": "123", "name": "Lại Hà Trang", "department": "KINH DOANH 2"},
    "nv256": {"password": "123", "name": "Bùi Thu Thảo", "department": "KINH DOANH 3"},
    "nv258": {"password": "123", "name": "Lê Thị Ngọc Anh", "department": "KINH DOANH 3"},
    "nv259": {"password": "123", "name": "Vũ Thị Hương", "department": "KINH DOANH 3"},
    "nv260": {"password": "123", "name": "Nguyễn Thu Hà", "department": "KINH DOANH 2"},
    "nv263": {"password": "123", "name": "Nguyễn Ngân Giang", "department": "KINH DOANH 2"},
    "nv264": {"password": "123", "name": "Đỗ Thị Diệu Linh", "department": "KINH DOANH 3"},
    "nv268": {"password": "123", "name": "Nguyễn Thị Phương Thảo", "department": "KINH DOANH 3"},
    "nv269": {"password": "123", "name": "Ngô Nam Thùy Trang", "department": "DỊCH VỤ KỸ THUẬT"},

    # ===== KINGS - NHÂN VIÊN NAM (39 người) =====
    "nv006": {"password": "123", "name": "Vũ Văn Nguyên", "department": "DỊCH VỤ KỸ THUẬT"},
    "nv018": {"password": "123", "name": "Tào Văn Hùng", "department": "BAN GIÁM ĐỐC"},
    "nv028": {"password": "123", "name": "Trần Viết Bốn", "department": "KHO VẬN"},
    "nv048": {"password": "123", "name": "Nguyễn Đình Anh", "department": "KHO VẬN"},
    "nv057": {"password": "123", "name": "Trần Huy Quang", "department": "MUA HÀNG"},
    "nv063": {"password": "123", "name": "Trần Mạnh Chiến", "department": "KHO VẬN"},
    "nv068": {"password": "123", "name": "Lê Thanh Toàn", "department": "DỊCH VỤ KỸ THUẬT"},
    "nv075": {"password": "123", "name": "Nguyễn Phương Tiến", "department": "KINH DOANH 2"},
    "nv076": {"password": "123", "name": "Hoàng Thanh Liêm", "department": "KINH DOANH 3"},
    "nv107": {"password": "123", "name": "Lê Thị Hồng Ngân", "department": "CÔNG NGHỆ"},
    "nv113": {"password": "123", "name": "Thạch Minh Đức", "department": "KHO VẬN"},
    "nv114": {"password": "123", "name": "Lê Đình Mạnh", "department": "DỊCH VỤ KỸ THUẬT"},
    "nv125": {"password": "123", "name": "Tào Tuệ Dũng", "department": "KINH DOANH 2"},
    "nv132": {"password": "123", "name": "Vũ Tiến Khôi", "department": "KHO VẬN"},
    "nv137": {"password": "123", "name": "Nguyễn Quốc Đạt", "department": "DỊCH VỤ KỸ THUẬT"},
    "nv141": {"password": "123", "name": "Vũ Thành Luân", "department": "KHO VẬN"},
    "nv157": {"password": "123", "name": "Nguyễn Tuấn Anh", "department": "KHO VẬN"},
    "nv163": {"password": "123", "name": "Đồng Thế Văn", "department": "DỊCH VỤ KỸ THUẬT"},
    "nv172": {"password": "123", "name": "Ngô Trí Công", "department": "KHO VẬN"},
    "nv176": {"password": "123", "name": "Bùi Huy Phúc", "department": "KHO VẬN"},
    "nv186": {"password": "123", "name": "Hoàng Văn Hải", "department": "DỊCH VỤ KỸ THUẬT"},
    "nv188": {"password": "123", "name": "Đỗ Hữu Quân", "department": "CÔNG NGHỆ"},
    "nv192": {"password": "123", "name": "Nguyễn Văn Sơn", "department": "KHO VẬN"},
    "nv209": {"password": "123", "name": "Đỗ Ngọc Nam", "department": "KHO VẬN"},
    "nv210": {"password": "123", "name": "Tăng Văn Dũng", "department": "KHO VẬN"},
    "nv215": {"password": "123", "name": "Đỗ Thị Thu Thảo", "department": "KINH DOANH 4"},
    "nv221": {"password": "123", "name": "Vũ Hiệp", "department": "KHO VẬN"},
    "nv228": {"password": "123", "name": "Nguyễn Quốc Đạt", "department": "KINH DOANH 1"},
    "nv236": {"password": "123", "name": "Vũ Duy Ba", "department": "KINH DOANH 6"},
    "nv237": {"password": "123", "name": "Trịnh Trung Dũng", "department": "CÔNG NGHỆ"},
    "nv247": {"password": "123", "name": "Trần Thị Lợi", "department": "HÀNH CHÍNH - NHÂN SỰ"},
    "nv261": {"password": "123", "name": "Nguyễn Đức Mạnh", "department": "DỊCH VỤ KỸ THUẬT"},
    "nv267": {"password": "123", "name": "Nguyễn Văn Đạt", "department": "CÔNG NGHỆ"},
}

# Tiết mục options - CẬP NHẬT MỚI
TIET_MUC_OPTIONS = [
    "ĐỘI 1 - KD3 - Giai điệu Việt nam mình",
    "KHO VẬN - Bách Liên ký",
    "ĐỘI 1 - KD2 - Brother Louie",
    "ĐẠI HỌC TỔNG HỢP - Tiếng khèn cùng chiếc khăn piêu",
    "KỸ THUẬT DỊCH VỤ - Hát vui tươi",
    "LIÊN ĐOÀN KINH DOANH - Hồn xưa khí mới",
    "KẾ TOÁN - Rạng Ngời Niềm Tin",
    "ĐỘI 2 - KD2 - Gió đánh đò đưa",
    "MUA HÀNG - Từ Linh Thiêng Đến Phong Trần",
    "ĐỘI 1 - KD3 - Lô Tô Bách Niên Show",
]

# KHÔNG CẦN HÌNH ẢNH NỮA - BỎ DICT NÀY
TIET_MUC_IMAGES = {}

TIET_MUC_SET = set(TIET_MUC_OPTIONS)

# Helper functions
def get_departments():
    """Lấy danh sách phòng ban và nhân viên"""
    departments = {}
    for username, info in NHAN_VIEN.items():
        dept = info["department"]
        departments.setdefault(dept, [])
        departments[dept].append({"username": username, "name": info["name"]})
    for dept in departments:
        departments[dept] = sorted(departments[dept], key=lambda x: x["name"])
    return departments

def get_kings_and_queens():
    """Phân loại nhân viên theo giới tính"""
    kings_depts = {}
    queens_depts = {}
    
    kings_list = [
        "nv006", "nv018", "nv028", "nv048", "nv057", "nv063", "nv068", 
        "nv075", "nv076", "nv113", "nv114", "nv125", "nv132", 
        "nv137", "nv141", "nv157", "nv163", "nv172", "nv176", "nv186",
        "nv188", "nv192", "nv209", "nv210", "nv221", "nv228",
        "nv236", "nv237", "nv261", "nv267"
    ]
    
    for username, info in NHAN_VIEN.items():
        dept = info["department"]
        if username in kings_list:
            kings_depts.setdefault(dept, [])
            kings_depts[dept].append({"username": username, "name": info["name"]})
        else:
            queens_depts.setdefault(dept, [])
            queens_depts[dept].append({"username": username, "name": info["name"]})
    
    for dept in kings_depts:
        kings_depts[dept] = sorted(kings_depts[dept], key=lambda x: x["name"])
    for dept in queens_depts:
        queens_depts[dept] = sorted(queens_depts[dept], key=lambda x: x["name"])
    
    return kings_depts, queens_depts

def get_forbidden_tiet_muc_for_department(dept: str) -> set:
    """Trả về tập các tiết mục mà user KHÔNG ĐƯỢC vote"""
    d = (dept or "").strip().upper()
    
    # KINH DOANH 1, 4, 6 → Không được vote "LIÊN ĐOÀN KINH DOANH"
    if d in ("KINH DOANH 1", "KINH DOANH 4", "KINH DOANH 6"):
        return {"LIÊN ĐOÀN KINH DOANH - Hồn xưa khí mới"}
    
    # CÔNG NGHỆ, MKT, KSNB, HCNS → Không được vote "ĐẠI HỌC TỔNG HỢP"
    if d in ("CÔNG NGHỆ", "MARKETING", "KINH DOANH SALES NỘI BỘ", "HÀNH CHÍNH - NHÂN SỰ"):
        return {"ĐẠI HỌC TỔNG HỢP - Tiếng khèn cùng chiếc khăn piêu"}
    
    # KINH DOANH 2 → Không được vote CẢ 2 tiết mục của KD2
    if d == "KINH DOANH 2":
        return {
            "ĐỘI 1 - KD2 - Brother Louie",
            "ĐỘI 2 - KD2 - Gió đánh đò đưa"
        }
    
    # KINH DOANH 3 → Không được vote CẢ 2 tiết mục của KD3
    if d == "KINH DOANH 3":
        return {
            "ĐỘI 1 - KD3 - Giai điệu Việt nam mình",
            "ĐỘI 1 - KD3 - Lô Tô Bách Niên Show"
        }
    
    # KHO VẬN
    if d == "KHO VẬN":
        return {"KHO VẬN - Bách Liên ký"}
    
    # KẾ TOÁN
    if d == "KẾ TOÁN":
        return {"KẾ TOÁN - Rạng Ngời Niềm Tin"}
    
    # DỊCH VỤ KỸ THUẬT
    if d == "DỊCH VỤ KỸ THUẬT":
        return {"KỸ THUẬT DỊCH VỤ - Hát vui tươi"}
    
    # MUA HÀNG
    if d == "MUA HÀNG":
        return {"MUA HÀNG - Từ Linh Thiêng Đến Phong Trần"}
    
    # BAN GIÁM ĐỐC - Không bị chặn gì
    if d == "BAN GIÁM ĐỐC":
        return set()
    
    # XUẤT NHẬP KHẨU - Không có tiết mục riêng nên không bị chặn
    if d == "XUẤT NHẬP KHẨU":
        return set()
    
    return set()

PHONG_BAN = get_departments()
KINGS_PHONG_BAN, QUEENS_PHONG_BAN = get_kings_and_queens()