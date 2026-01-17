# 💀 NTFS Zombie Hunter Pro 💀
[![Version](https://img.shields.io/badge/version-1.1.0--Ultimate-red.svg)](https://github.com/Thanhnguyen123-men/Scanner)
[![Platform](https://img.shields.io/badge/platform-Windows-blue.svg)](https://www.microsoft.com/windows)

> **Công cụ Forensic mạnh mẽ chuyên phát hiện và nhận diện các thực thể "Không Thể kill" (Zombie/Junction) trên hệ thống tệp NTFS.**

---

## 🚀 Tính năng nổi bật
- **NTFS Deep Scan**: Thuật toán quét sâu hiệu năng cao, tối ưu cho các ổ đĩa lớn.
- **Zombie & Reparse Point Detection**: Nhận diện chính xác Junction, Symbolic Link và các liên kết bị hỏng (Zombies).
- **Dual Mode Support**:
  - **Standard Edition**: Quét nhanh các thư mục dữ liệu người dùng.
  - **Admin Edition**: Toàn quyền truy cập để quét các vùng hệ thống nhạy cảm (C:\, Windows...).
- **Modern Dark UI**: Giao diện trực quan, chuyên nghiệp với thanh tiến trình thực tế.

## 🛠 Bộ công cụ đóng gói (Release)
| File | Chức năng | Quyền hạn |
| :--- | :--- | :--- |
| `Hunter_Ultimate.exe` | Quét thư mục dữ liệu thường | Standard User |
| `Hunter_Ultimate_ADMIN.exe` | Quét toàn bộ hệ thống (có khiên) | Administrator |
| `info.txt` | Thông số kỹ thuật & Phiên bản | - |
| `TERMS_OF_USE.txt` | Điều khoản miễn trừ trách nhiệm , khi mày nghịch sai | - |

## 📖 Hướng dẫn nhanh
1. Tải bản Release mới nhất từ thư mục `dist`.
2. Sử dụng bản **Standard** cho các tác vụ thông thường.
3. Sử dụng bản **ADMIN** để truy cập sâu vào các folder hệ thống (giúp đọc đúng các mã TAG như `0xa0000003`).

## ⚠️ Miễn trừ trách nhiệm
Dự án được thực hiện bởi **ThanhNguyen**. Người dùng hoàn toàn chịu trách nhiệm về mọi rủi ro khi sử dụng công cụ này trên hệ thống thực tế. Vui lòng đọc kỹ `TERMS_OF_USE.txt`.

---
**Developed by ThanhNguyen** 🛡️🔥
--
> [!TIP]
> Nếu bạn không muốn tải tool, có thể dùng lệnh Windows gốc:
> `chkdsk C: /f /r /x` (Chạy với quyền Administrator).
> VÀ nếu nó ở chỗ khác ví dụ : D:\abc\..\node
> Thì nhập `CHKDSK D: /f /r /x`
