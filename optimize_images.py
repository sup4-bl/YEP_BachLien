"""
Script tối ưu hóa ảnh nhân viên cho YEP Voting
- Resize về kích thước chuẩn
- Nén chất lượng
- Chuyển sang WebP (nhẹ hơn 30-50%)
"""

from PIL import Image
import os
from pathlib import Path

# Cấu hình
INPUT_DIR = "static/img/people"
OUTPUT_DIR = "static/img/people_optimized"
TARGET_SIZE = (200, 200)  # Avatar chỉ cần 200x200px
QUALITY = 85  # Chất lượng nén (70-90 là tốt)
CONVERT_TO_WEBP = True  # WebP nhẹ hơn JPG/PNG 30-50%

def optimize_image(input_path, output_path):
    """Tối ưu 1 ảnh"""
    try:
        with Image.open(input_path) as img:
            # Convert sang RGB nếu là PNG có alpha
            if img.mode in ('RGBA', 'LA', 'P'):
                # Tạo background trắng
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = background
            elif img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Resize về kích thước chuẩn (dùng LANCZOS để giữ chất lượng)
            img.thumbnail(TARGET_SIZE, Image.Resampling.LANCZOS)
            
            # Xác định định dạng output
            if CONVERT_TO_WEBP:
                output_path = output_path.with_suffix('.webp')
                img.save(output_path, 'WEBP', quality=QUALITY, method=6)
            else:
                img.save(output_path, 'JPEG', quality=QUALITY, optimize=True)
            
            # So sánh kích thước file
            original_size = os.path.getsize(input_path)
            new_size = os.path.getsize(output_path)
            reduction = (1 - new_size/original_size) * 100
            
            print(f"✓ {input_path.name}: {original_size//1024}KB → {new_size//1024}KB ({reduction:.1f}% nhỏ hơn)")
            return True
            
    except Exception as e:
        print(f"✗ Lỗi xử lý {input_path.name}: {e}")
        return False

def main():
    input_dir = Path(INPUT_DIR)
    output_dir = Path(OUTPUT_DIR)
    
    # Tạo thư mục output
    output_dir.mkdir(exist_ok=True)
    
    # Các định dạng ảnh cần xử lý
    image_extensions = {'.jpg', '.jpeg', '.png', '.webp', '.JPG', '.JPEG', '.PNG', '.WEBP'}
    
    # Lấy danh sách ảnh
    images = [f for f in input_dir.iterdir() 
              if f.is_file() and f.suffix in image_extensions]
    
    if not images:
        print(f"❌ Không tìm thấy ảnh trong {INPUT_DIR}")
        return
    
    print(f"🔧 Tìm thấy {len(images)} ảnh cần tối ưu")
    print(f"📐 Resize: {TARGET_SIZE[0]}x{TARGET_SIZE[1]}px")
    print(f"🎨 Chất lượng: {QUALITY}%")
    print(f"📦 Format: {'WebP' if CONVERT_TO_WEBP else 'JPEG'}")
    print("-" * 60)
    
    success_count = 0
    total_original = 0
    total_new = 0
    
    for img_path in images:
        # Giữ nguyên tên file (chỉ đổi extension nếu convert WebP)
        output_path = output_dir / img_path.name
        
        if optimize_image(img_path, output_path):
            success_count += 1
            total_original += os.path.getsize(img_path)
            
            # Tìm file output (có thể đã đổi extension)
            output_files = list(output_dir.glob(f"{img_path.stem}.*"))
            if output_files:
                total_new += os.path.getsize(output_files[0])
    
    print("-" * 60)
    print(f"✅ Hoàn thành: {success_count}/{len(images)} ảnh")
    print(f"💾 Tổng dung lượng: {total_original//1024}KB → {total_new//1024}KB")
    print(f"📉 Tiết kiệm: {(1 - total_new/total_original)*100:.1f}%")
    print(f"\n📁 Ảnh đã tối ưu trong: {output_dir}")
    print(f"\n⚠️  Sau khi kiểm tra, thay thế thư mục {INPUT_DIR} bằng {OUTPUT_DIR}")

if __name__ == "__main__":
    main()