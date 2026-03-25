# 🔥 NTFS Zombie Hunter Pro 🔥 
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
> sau đó restart máy (**ĐỪNG TẮT MÁY NẾU KHÔNG DÍNH THÊM BUG RÁNG CHỊU**)
> nếu ko triệt hạ được thì..... cố tìm phương pháp khác
--

> {TIP ngoài lề}
**Bro muốn có một trang web riêng để "khè" dự án nhưng méo có tiền mua tên miền và hosting? Yên tâm, đã có Netlify lo**
1. Truy cập: https://app.netlify.com/
2. Chỉ việc ném folder code (HTML/JS) vào mục Deploy.
3. Chỉnh tên miền tùy ý theo dạng: ten-cua-bro.netlify.app
4. Thế là xong, có ngay web xịn, load nhanh mà quan trọng là FREE!
> KHÔNG HIỂU THỨ GÌ THÌ DÙNG CHAT-BOT-AI để hỏi :)
- Gé thăm một chút về bot discord của tui : `https://moderationskibidi.netlify.app/`
# lý do build
> đơn giản là từng bị 1 folder zombie lỗi cấp NTFS , nó mạnh đến mức `del` hay `rd` , `move` cũng không có tác dụng ngay cả WinRE (cmd) hoặc cmd quyền TrustedInstaler
> khi dùng đòn chkdsk thì mới thành công xóa nó (trường hợp khác giống tui là vẫn còn nhưng xóa đc )
> đơn giản vậy thôi :)
# Bằng chứng SHA 256
<img width="1385" height="855" alt="image" src="https://github.com/user-attachments/assets/2ba2753f-eb1e-4285-a654-6d6dde877917" />
Dùng lệnh ở powershell (phải đúng chỗ tải file) và 

**TUYỆT ĐỐI File phải là bản gốc, chưa chỉnh sửa, tải trực tiếp từ repo thì SHA-256 mới khớp** 

`chứ chỉnh sửa dù 1 dòng command ở ở source code sẽ làm thay đổi SHA 256 dù 1 chút`

> `Get-FileHash Hunter_Ultimate.exe, Hunter_Ultimate_ADMINISTRATOR.exe | Format-Table -AutoSize`

> Admin : `98F38F86F76ACA29E8C58182CA5D7A8DF1A6FF5D1D71E192F35C97A69D17C240`

> Level Users : `4E810CC1F772CBF6ADC8A4D8543FAE3CB9E37B4EE2B4BB70EAAD8C75B57EE143`

___________________________________________________________________________________________

# UPDATE

Bản v1.4.7 đã thêm Digital Signatures nên SHA256 cập nhật là

> `Scanner.exe` : `CD11620B27608342B0529BA994A67D5ADE879BAF15B0963E25B2A2B014B7E707`

> `Scanner_Administrator.exe` : `007CFE465FC409D75D782D479112B4BA9CFE719E33A2B08134929C610EA931A5`
