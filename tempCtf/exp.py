from pwn import *
import base64


conn = remote('chal.pctf.competitivecyber.club', 9001)

def base64_decode(data, n):
    for i in range(n):
        data = base64.b64decode(data).decode()
    return data

for i in range(0, 1001):
    
    conn.recvuntil(b'Challenge: ')
    base64_data = conn.recvline().strip()
    d_base64 = base64.b64decode(base64_data).decode()
    n = int(d_base64.split('|')[1])
    decoded_data = base64_decode(d_base64.split('|')[0], n)
    response = f"{decoded_data}|{i}"
    conn.sendlineafter(b'>> ', response.encode())


conn.close()