from math import gcd

# Hàm tìm nghịch đảo modulo của a trong modulo m
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Hàm mã hóa Affine
def affine_encode(text, a, b):
    m = 26  # Kích thước bảng chữ cái tiếng Anh
    # Kiểm tra rằng a và m là nguyên tố cùng nhau
    if gcd(a, m) != 1:
        raise ValueError("Giá trị 'a' phải nguyên tố cùng m để mã hóa Affine.")

    encoded_text = ""
    for char in text:
        if char.isalpha():  # Mã hóa chỉ các ký tự chữ cái
            # Chuyển đổi ký tự sang mã ASCII và mã hóa
            start = ord('A') if char.isupper() else ord('a')
            x = ord(char) - start
            encoded_char = (a * x + b) % m + start
            encoded_text += chr(encoded_char)
        else:
            # Giữ nguyên ký tự không phải chữ cái
            encoded_text += char
    return encoded_text

# Hàm giải mã Affine
def affine_decode(cipher_text, a, b):
    m = 26
    a_inv = mod_inverse(a, m)
    try:
        if a_inv is None:
            raise ValueError("Không tồn tại nghịch đảo của 'a' trong modulo m, không thể giải mã.")
    except ValueError as e:
        print(f"Lỗi mã hóa: {e}")
        return text

    decoded_text = ""
    for char in cipher_text:
        if char.isalpha():
            # Chuyển đổi ký tự sang mã ASCII và giải mã
            start = ord('A') if char.isupper() else ord('a')
            y = ord(char) - start
            decoded_char = (a_inv * (y - b)) % m + start
            decoded_text += chr(decoded_char)
        else:
            decoded_text += char
    return decoded_text

c = 'Hg hz qhrf gxydp'
for i in range(1, 10):
    for j in range(1, 10):
        p = affine_decode(c, i, j)
        print(f"({i}, {j}) -> {p}")

