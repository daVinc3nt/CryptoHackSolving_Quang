# SESSION 2

## Privacy vs Secret vs Confidential

### 🔹 Privacy (Quyền riêng tư)
- **Định nghĩa**: Quyền kiểm soát dữ liệu cá nhân, thông tin định danh, và cách thông tin đó được thu thập, lưu trữ, chia sẻ.  
- **Ví dụ**:  
  - Email, số điện thoại, vị trí GPS.  
  - GDPR (Châu Âu) hay Luật bảo vệ dữ liệu cá nhân VN.  
- **Tính chất**: Nói về **quyền** của cá nhân và **nguyên tắc xử lý dữ liệu**.  

### 🔹 Secret (Bí mật tuyệt đối / Tối mật)
- **Định nghĩa**: Thông tin chỉ một số rất ít người biết, không được tiết lộ ra ngoài. Nếu lộ → có thể gây nguy hiểm trực tiếp hoặc mất kiểm soát.  
- **Ví dụ**:  
  - Mật khẩu, private key trong cryptography.  
  - Mã phóng tên lửa, công thức Coca-Cola.  
- **Tính chất**: Chỉ một phạm vi hẹp được biết (nguyên tắc “need-to-know”).  

### 🔹 Confidential (Thông tin mật / Bảo mật)
- **Định nghĩa**: Thông tin nhạy cảm cần bảo vệ, chỉ cho phép chia sẻ trong một phạm vi được ủy quyền, nhưng không “tuyệt mật” như secret.  
- **Ví dụ**:  
  - Hợp đồng kinh doanh, kế hoạch chiến lược.  
  - Hồ sơ nhân sự, báo cáo tài chính nội bộ.  
- **Tính chất**: Cần bảo vệ để tránh thiệt hại (thương mại, pháp lý), nhưng nhiều người trong tổ chức có thể được phép truy cập.  

### 📝 Tóm gọn phân biệt
| Thuật ngữ       | Ý nghĩa chính            | Đặc điểm                                   | Ví dụ                                |
|-----------------|--------------------------|-------------------------------------------|--------------------------------------|
| **Privacy**     | Quyền riêng tư cá nhân   | Kiểm soát dữ liệu cá nhân, tuân luật       | Email, số CMND, vị trí GPS           |
| **Secret**      | Bí mật tuyệt đối         | Cực kỳ giới hạn, nếu lộ gây nguy hại trực tiếp | Mật khẩu, private key                |
| **Confidential**| Thông tin mật            | Nhạy cảm, chia sẻ trong phạm vi cho phép  | Hợp đồng kinh doanh, hồ sơ nhân sự   |

---

## Encoding vs Encrypting

### 🔹 Encoding (Mã hóa để biểu diễn)
- **Mục đích**: Biến dữ liệu sang định dạng khác để **truyền tải/lưu trữ dễ dàng**, không nhằm bảo mật.  
- **Đặc điểm**: Có thể đảo ngược dễ dàng, **không cần key**.  
- **Ví dụ**:  
  - Base64 (biến dữ liệu nhị phân thành ký tự).  
  - ASCII, UTF-8.  
  - URL encoding (`space → %20`).  

### 🔹 Encrypting (Mã hóa để bảo mật)
- **Mục đích**: Biến dữ liệu thành dạng không đọc được để **bảo vệ bí mật**.  
- **Đặc điểm**: Cần **key** để giải mã (decrypt).  
- **Ví dụ**:  
  - AES, RSA, ChaCha20.  
  - HTTPS dùng TLS.  

### 📝 Tóm gọn
| Thuật ngữ        | Mục đích chính                           | Có bảo mật không? | Cần key không? | Ví dụ                  |
|------------------|------------------------------------------|------------------|----------------|------------------------|
| **Encoding**     | Chuyển đổi định dạng để lưu/truyền dữ liệu | ❌ Không          | ❌ Không        | Base64, UTF-8, URL encode |
| **Encrypting**   | Bảo mật dữ liệu, ngăn đọc trái phép       | ✅ Có             | ✅ Có           | AES, RSA, TLS          |

---

## Cryptology vs Cryptography vs Cryptanalysis

### 🔹 Cryptology
- **Định nghĩa**: Ngành khoa học tổng quát nghiên cứu về bí mật thông tin.  
- **Bao gồm 2 nhánh**:  
  1. **Cryptography** → tạo hệ thống mã hóa, bảo mật.  
  2. **Cryptanalysis** → phân tích, phá mã.  
- **Ví dụ**: Nhà nghiên cứu cryptology có thể vừa phát triển thuật toán, vừa nghiên cứu cách tấn công nó.  

### 🔹 Cryptography
- **Định nghĩa**: Nhánh của cryptology tập trung vào thiết kế mã hóa để bảo vệ thông tin.  
- **Mục tiêu**: Đảm bảo 4 tính chất:  
  - Confidentiality (bí mật)  
  - Integrity (toàn vẹn)  
  - Authentication (xác thực)  
  - Non-repudiation (chống chối bỏ)  
- **Ví dụ**: AES, RSA, TLS, chữ ký số.  

### 🔹 Cryptanalysis
- **Định nghĩa**: Nhánh của cryptology chuyên về **phá mã** – tìm điểm yếu, kỹ thuật để giải mã thông tin **mà không có key hợp lệ**.  
- **Mục tiêu**: Đánh giá, thử thách mức độ an toàn của hệ thống mật mã.  
- **Ví dụ**: Phân tích tần suất để phá Caesar cipher; tấn công side-channel lên AES; brute force RSA key yếu.  

### 🔹 Cryptanalyst
- **Định nghĩa**: Người thực hiện **cryptanalysis**.  
- **Vai trò**:  
  - Trong quân sự: giải mã thông tin liên lạc đối phương (ví dụ: Alan Turing phá Enigma).  
  - Trong hiện đại: chuyên gia bảo mật thử nghiệm, đánh giá, và phát hiện lỗ hổng của hệ thống mã hóa.  
- **Ví dụ**: Cryptanalyst có thể nghiên cứu xem một thuật toán hash có bị “collision attack” hay không.  
---

# Cryptographic Concepts: Primitive vs Building Block vs Scheme vs Protocol vs System

## 🔹 1. Cryptographic Primitive
- **Định nghĩa**: Các **thành phần cơ bản nhất** trong mật mã, giống “nguyên tử” để xây hệ thống.  
- **Ví dụ**:  
  - Hàm băm (hash function).  
  - Khóa công khai / khóa bí mật.  
  - Block cipher (AES), stream cipher.  
  - Pseudorandom generator (PRG).  
- **Đặc điểm**: Đơn giản, không trực tiếp giải quyết toàn bộ nhu cầu bảo mật, nhưng làm nền tảng.  

---

## 🔹 2. Cryptographic Building Block
- **Định nghĩa**: Thành phần **tầm trung**, được xây dựng từ primitive, dùng để tạo ra các cấu trúc lớn hơn.  
- **Ví dụ**:  
  - Message Authentication Code (MAC) (có thể xây từ hash + key).  
  - Digital Signature (dùng hash + asymmetric encryption).  
  - Key exchange building block (Diffie–Hellman).  
- **Đặc điểm**: Có thể coi là “lego” ghép từ primitive, tái sử dụng trong nhiều thiết kế.  

---

## 🔹 3. Cryptographic Scheme
- **Định nghĩa**: Một **hệ mật mã hoàn chỉnh** cho một tác vụ bảo mật cụ thể, được mô tả bởi các thuật toán (KeyGen, Encrypt, Decrypt, Sign, Verify...).  
- **Ví dụ**:  
  - RSA Encryption Scheme.  
  - ElGamal Signature Scheme.  
  - AES-GCM scheme (encryption + authentication).  
- **Đặc điểm**: Có định nghĩa hình thức và chứng minh an toàn (provable security).  

---

## 🔹 4. Cryptographic Protocol
- **Định nghĩa**: Cách nhiều scheme và building block được **phối hợp trong môi trường thực tế** để đạt mục tiêu bảo mật phức tạp hơn.  
- **Ví dụ**:  
  - TLS/SSL protocol (sử dụng key exchange + digital signature + symmetric encryption).  
  - Signal protocol (dùng Double Ratchet, Diffie–Hellman, AES).  
  - Kerberos authentication protocol.  
- **Đặc điểm**: Hoạt động ở mức ứng dụng, nhiều bước giao tiếp, có thể dùng nhiều scheme.  

---

## 🔹 5. Cryptographic System
- **Định nghĩa**: Một **hệ thống thực tế** áp dụng nhiều protocol để vận hành trong đời sống hoặc doanh nghiệp.  
- **Ví dụ**:  
  - **Online Banking System**: dùng TLS để bảo mật kết nối, RSA/ECC để xác thực, AES để mã hóa dữ liệu.  
  - **E-commerce Platform**: tích hợp HTTPS (TLS), chữ ký số cho giao dịch, token cho xác thực.  
  - **Blockchain System**: kết hợp hash, chữ ký số, consensus protocol.  
- **Đặc điểm**: Là sản phẩm/ứng dụng hoàn chỉnh, đưa các protocol vào thực tế.  

---

## 📝 Tóm gọn phân biệt
| Tầng             | Ý nghĩa                                     | Ví dụ                                    |
|------------------|---------------------------------------------|------------------------------------------|
| **Primitive**    | Thành phần cơ bản nhất (nguyên tử)          | AES, SHA-256, PRG                        |
| **Building Block** | Cấu trúc trung gian từ primitive          | MAC, Digital Signature, DH key exchange  |
| **Scheme**       | Hệ mật mã cụ thể, gồm thuật toán và chứng minh | RSA scheme, ElGamal scheme, AES-GCM     |
| **Protocol**     | Giao tiếp hoàn chỉnh, dùng nhiều scheme     | TLS, Signal, Kerberos                    |
| **System**       | Hệ thống ứng dụng thực tế, dùng nhiều protocol | Online Banking, Blockchain, E-commerce   |

---

👉 Dễ nhớ như kim tự tháp:  
- **Primitive** = nguyên tử 🔬  
- **Building Block** = mảnh lego 🧩  
- **Scheme** = bộ sản phẩm 📦  
- **Protocol** = luật chơi/giao tiếp 🌐  
- **System** = ứng dụng thực tế 🏦  
