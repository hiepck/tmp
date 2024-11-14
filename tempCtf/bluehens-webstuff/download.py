import os

# Đọc các URL từ file.txt
with open('file.txt', 'r') as file:
    urls = file.readlines()

# Loại bỏ ký tự xuống dòng và khoảng trắng thừa
urls = [url.strip() for url in urls if url.strip()]

# Tải từng file từ các URL bằng lệnh wget
target = 'https://bluehens-webstuff.chals.io/'
for url in urls:
    os.system(f"wget {target}{url}")

