def encode(p):
    for i in range(0, len(p)):
        char = p[i]
        # Kiểm tra nếu ký tự là chữ cái
        if char.isalpha():
            # Chuyển đổi ký tự sang mã ASCII và dịch chuyển k vị trí
            # 'A' cho chữ in hoa (ord('A') == 65)
            shifted = (ord(char) - ord('A') + k) % 26 + ord('A')
            a += chr(shifted)
        else:
            # Giữ nguyên ký tự nếu không phải là chữ cái (ví dụ: khoảng trắng)
            a += char
    return a

def decode(cipher_text, shift):
    decrypted_text = ""
    for char in cipher_text:
        # Kiểm tra nếu ký tự là chữ cái
        if char.isalpha():
            # Xác định điểm bắt đầu: 'A' cho chữ hoa và 'a' cho chữ thường
            start = ord('A') if char.isupper() else ord('a')
            # Dịch ngược ký tự với khoảng dịch chuyển
            decrypted_char = (ord(char) - start - shift) % 26 + start
            decrypted_text += chr(decrypted_char)
        else:
            # Giữ nguyên ký tự không phải chữ cái
            decrypted_text += char
    return decrypted_text

c = 'Hg hz qhrf gxydp'
p = ''
i = 1
while True:
    p = decode(c, i)
    print(f"Dang thu lan thu {i}", end="\r")
    if 'It' in p:
        print(p)
        break
    i = i + 1







