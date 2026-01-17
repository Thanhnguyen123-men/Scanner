# 💀 NTFS Zombie Hunter Pro 💀
[![Version](https://img.shields.io/badge/version-1.1.0--Ultimate-red.svg)](https://github.com/Thanhnguyen123-men/Scanner)
[![Platform](https://img.shields.io/badge/platform-Windows-blue.svg)](https://www.microsoft.com/windows)

> **Công cụ Forensic mạnh mẽ chuyên phát hiện và nhận diện các thực thể "Không Thể kill" (Zombie/Junction) trên hệ thống tệp NTFS.**

---

## 🚀 Tính năng nổi bật đã được thêm như :
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
| `TERMS_OF_USE.txt` | Điều khoản miễn trừ trách nhiệm (đọc trước khi nghịch) | - |

## 📖 Hướng dẫn nhanh
1. Tải bản Release mới nhất từ thư mục `dist`.
2. Sử dụng bản **Standard** cho các tác vụ thông thường.
3. Sử dụng bản **ADMIN** để truy cập sâu vào các folder hệ thống (giúp đọc đúng các mã TAG như `0xa0000003`).

## 🗣 LƯU Ý 
- Tool này chỉ "sủa" – nó phát hiện và báo cáo.
- Bạn thấy Windows SmartScreen có thể cảnh báo vì ứng dụng **chưa được ký chứng chỉ** thì kệ mom nó vì nó rất bình thường `(do app tự build chưa mua chứng chỉ mà muốn có thì phải có tiền mà bro biết tui làm méo gì có tiền :( )`
- Bấm **More info** rồi bấn **Run anyway** 
- đợi 1 chút rồi sẽ có thành phẩm :) 
- UAC ( user account control ) Nó hỏi thì cứ bấn "OK"
- Quyết định xử lý hay không là việc của bạn. `(cách khuyên dùng là CHKDSK ở mục !TIP)`

![Screenshot 2026-01-17 073835](https://github.com/user-attachments/assets/5858f124-8d7c-407e-8d94-2dd06d06e78c)

<img width="777" height="532" alt="image" src="https://github.com/user-attachments/assets/53a5fe03-677f-49bf-a9ef-bbe7e9d77e5a" />

## ⚠️ Miễn trừ trách nhiệm
Dự án được thực hiện bởi **ThanhNguyen**. Người dùng hoàn toàn chịu trách nhiệm về mọi rủi ro khi sử dụng công cụ này trên hệ thống thực tế. Vui lòng đọc kỹ `TERMS_OF_USE.txt`.

---
**Developed by ThanhNguyen** 🛡️🔥
--
## SOCIAL DEV
- Youtube : `https://www.youtube.com/@ThanhNguyen_17345`
- Discord ID account : `1379310041903140895`
- Github : CHỖ NÀY 🤣 `https://github.com/Thanhnguyen123-men`
- Website (non-DNS private) : `https://sites.google.com/view/thanhnguyen-vn/trang-ch%E1%BB%A7`
--
> [!TIP]
> Nếu bạn không muốn tải tool, có thể dùng lệnh Windows gốc:
> `chkdsk C: /f /r /x` (Chạy với quyền Administrator).
> VÀ nếu nó ở chỗ khác ví dụ : D:\abc\..\node
> Thì nhập `CHKDSK D: /f /r /x`
--
> {TIP ngoài lề}
**Bro muốn có một trang web riêng để "khè" dự án nhưng méo có tiền mua tên miền và hosting? Yên tâm, đã có Netlify lo**
1. Truy cập: https://app.netlify.com/
2. Chỉ việc ném folder code (HTML/JS) vào mục Deploy.
3. Chỉnh tên miền tùy ý theo dạng: ten-cua-bro.netlify.app
4. Thế là xong, có ngay web xịn, load nhanh mà quan trọng là FREE!
> KHÔNG HIỂU THỨ GÌ THÌ DÙNG CHAT-BOT-AI để hỏi :)
- Gé thăm một chút về bot discord của tui : `https://moderationskibidi.netlify.app/`
