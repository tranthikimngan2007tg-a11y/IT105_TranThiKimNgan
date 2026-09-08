# Bài 2 — Phát hiện lỗi logic trong Quy trình Thanh toán QR VNPay

## Phần 1 — Phân tích lỗi sai AS-IS

Mô tả sơ đồ lỗi của BA: *"Hệ thống lập tức trừ tiền rồi mới kiểm tra mã QR, và bắt khách hàng chờ hệ thống gửi email xong thì mới chịu hiển thị báo thành công trên App."*

### Lỗi 1: Sai thứ tự trừ tiền (vi phạm Quy tắc 1 — Trừ tiền an toàn)

- Quy tắc nghiệp vụ yêu cầu: *"Hệ thống chỉ được phép gọi API trừ tiền KHI VÀ CHỈ KHI đã xác minh mã QR hoàn toàn hợp lệ."*
- BA lại thiết kế **trừ tiền trước, kiểm tra QR sau** → đây là lỗi logic nghiêm trọng về an toàn tài chính: nếu mã QR sai hoặc hết hạn (bẫy 15 phút), hệ thống đã lỡ trừ tiền của khách, gây tổn thất và tranh chấp.
- **Sửa:** phải đặt **nút Decision "QR hợp lệ và còn hạn?"** ngay sau bước quét mã, **trước** bước gọi API trừ tiền. Chỉ khi nhánh "Hợp lệ" được chọn thì luồng mới đi tới hành động trừ tiền; nhánh "Không hợp lệ/hết hạn" phải rẽ thẳng sang từ chối giao dịch, không được đụng đến hành động trừ tiền.

### Lỗi 2: Xử lý tuần tự thay vì song song (vi phạm Quy tắc 2 — Xử lý song song)

- Quy tắc nghiệp vụ yêu cầu hệ thống phải làm **đồng thời** 2 việc sau khi trừ tiền thành công: (1) hiển thị màn hình thành công, (2) gửi email biên lai.
- BA lại thiết kế theo kiểu **tuần tự (sequential)**: chờ gửi email xong mới hiển thị thành công → gây độ trễ không cần thiết cho trải nghiệm người dùng, trong khi việc gửi email không có lý do gì phải chặn (block) việc hiển thị kết quả trên App.
- **Sửa:** dùng cặp **Fork/Join**. Sau khi trừ tiền thành công, Fork tách thành 2 nhánh chạy song song: "Hiển thị màn hình Thành công" và "Gửi email biên lai (chạy ngầm)". Có thể dùng Join để gộp lại trước khi kết thúc luồng (hoặc để 2 nhánh tự kết thúc độc lập nếu không cần đồng bộ tiếp).

## Phần 2 — Activity Diagram TO-BE

Xem file: `activity_diagram.drawio`

**Luồng chuẩn:**
```
Start
 → Khách quét mã QR
 → [Decision: QR hợp lệ và còn hạn (<=15 phút)?]
     ├─ Không hợp lệ/hết hạn → Từ chối giao dịch, yêu cầu lấy mã mới → End
     └─ Hợp lệ → Gọi API trừ tiền
                    → [Fork]
                        ├─ Hiển thị màn hình Thành công (App)
                        └─ Gửi email biên lai (chạy ngầm)
                    → [Join] → End
```
