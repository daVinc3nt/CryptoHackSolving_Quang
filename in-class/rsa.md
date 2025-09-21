# 🔹 RSA (Rivest–Shamir–Adleman)

(Có đi thi nha, tính tay)
## 1. Ý tưởng
RSA dùng **2 khóa**:  
- **Khóa công khai (public key)** để **mã hóa** (ai cũng biết).  
- **Khóa bí mật (private key)** để **giải mã** (chỉ chủ sở hữu biết).  

Điểm mấu chốt:  
- Dễ tính toán `m^e mod n`.  
- Nhưng cực khó để **tính ngược** nếu không biết `d`.  

---

## 2. Các bước với ví dụ nhỏ

### 🔑 Bước 1: Chọn số nguyên tố
- `p = 61`  
- `q = 53`

### 🔑 Bước 2: Tính n và φ(n)
- `n = p × q = 61 × 53 = 3233`  
- `φ(n) = (p-1)(q-1) = 60 × 52 = 3120`

### 🔑 Bước 3: Chọn e
- Chọn `e = 17` (thỏa gcd(e, φ(n)) = 1).  

### 🔑 Bước 4: Tính d
- Giải phương trình `(d × e) mod φ(n) = 1`  
- Tìm được `d = 2753`.  

👉 Kết quả:  
- **Public key** = `(n=3233, e=17)`  
- **Private key** = `(n=3233, d=2753)`  

---

## 3. Mã hóa và Giải mã
### Mã hóa
c = m^e mod n
c = 65^17 mod 3233 = 2790

markdown
Copy code
👉 Bản mã = **2790**

### Giải mã
m = c^d mod n
m = 2790^2753 mod 3233 = 65

python
Copy code
👉 Thu lại bản rõ = **65**

---

## 4. Chữ ký số
- Ký: `s = m^d mod n` (dùng private key).  
- Verify: `m = s^e mod n` (dùng public key).  

👉 Đảm bảo người ký thật sự sở hữu private key.  

---

## 5. Ví dụ đời thường
RSA giống như **hộp thư khóa**:  
- Ai cũng có thể bỏ thư vào (public key).  
- Chỉ bạn có chìa khóa riêng để mở (private key).  
- Ngược lại, chữ ký số giống như bạn **dùng chìa khóa riêng để ký** và mọi người dùng ổ khóa công khai để xác minh.  

---

## 6. Full Demo Code (Python)

```python
import random
from math import gcd

# -------------------------
# Helper: Nghịch đảo modular
# -------------------------
def modinv(a, m):
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
    g, x, _ = egcd(a, m)
    if g != 1:
        raise Exception('Không tồn tại nghịch đảo modular')
    return x % m

# -------------------------
# Sinh số nguyên tố nhỏ (demo)
# -------------------------
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime(start=50, end=200):
    while True:
        p = random.randint(start, end)
        if is_prime(p):
            return p

# -------------------------
# Tạo khóa RSA
# -------------------------
def generate_keys():
    p = generate_prime()
    q = generate_prime()
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537
    if gcd(e, phi) != 1:
        e = 3
        while gcd(e, phi) != 1:
            e += 2

    d = modinv(e, phi)
    return (n, e), (n, d)

# -------------------------
# Mã hóa & Giải mã
# -------------------------
def encrypt(pub, plaintext):
    n, e = pub
    return [pow(ord(ch), e, n) for ch in plaintext]

def decrypt(priv, ciphertext):
    n, d = priv
    return ''.join([chr(pow(c, d, n)) for c in ciphertext])

# -------------------------
# Chữ ký số
# -------------------------
def sign(priv, message):
    n, d = priv
    m = sum(ord(ch) for ch in message)  # hash demo
    return pow(m, d, n)

def verify(pub, message, signature):
    n, e = pub
    m = sum(ord(ch) for ch in message)
    return m == pow(signature, e, n)

# -------------------------
# Demo
# -------------------------
if __name__ == "__main__":
    public, private = generate_keys()
    print("Public key:", public)
    print("Private key:", private)

    msg = "HELLO"
    print("\nOriginal message:", msg)

    encrypted = encrypt(public, msg)
    print("Encrypted:", encrypted)

    decrypted = decrypt(private, encrypted)
    print("Decrypted:", decrypted)

    signature = sign(private, msg)
    print("\nSignature:", signature)
    print("Verify:", verify(public, msg, signature))