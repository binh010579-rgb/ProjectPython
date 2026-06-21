"""
Script tạo cấu trúc thư mục cho dự án ProjectPython.
Chạy 1 lần duy nhất ở thư mục gốc của repo (nơi có README.md, .gitignore).

Cách dùng:
    python setup_structure.py
"""

import os

folders = [
    "config",                  # file config (db, path...)
    "data/raw",                # dữ liệu thô - Thành viên 1 (KHÔNG commit lên git)
    "data/processed",          # dữ liệu đã làm sạch - Thành viên 3
    "data/stopwords",          # danh sách stopwords tiếng Việt
    "src/crawler",             # code crawl dữ liệu - Thành viên 1
    "src/database",            # code tạo bảng + import MySQL - Thành viên 2
    "src/preprocessing",       # code làm sạch dữ liệu - Thành viên 3
    "src/analysis",            # code phân tích, vẽ biểu đồ - Thành viên 4
    "src/app",                 # main.py + Streamlit dashboard - Thành viên 5
    "notebooks",                # các file .ipynb dùng để thử nghiệm
    "reports",                  # báo cáo Word cuối kỳ
    "outputs/charts",           # ảnh biểu đồ xuất ra
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    # Git không track thư mục rỗng -> tạo file .gitkeep để giữ thư mục
    if not os.listdir(folder):
        open(os.path.join(folder, ".gitkeep"), "w").close()

print("Đã tạo xong cấu trúc thư mục:\n")
for folder in folders:
    print(" -", folder)
