# Bài 1 — Phân tích & Sửa lỗi Sơ đồ Use Case (Đặt hàng & Áp dụng mã giảm giá)

## Phần 1 — Phân tích lỗi sai AS-IS

Mô tả của BA tập sự: *"Từ Đặt hàng, tôi vẽ mũi tên `«extend»` hướng tới Kiểm tra giỏ hàng. Từ Áp dụng mã giảm giá, tôi vẽ mũi tên `«include»` hướng về Đặt hàng."*

### Lỗi 1: "Đặt hàng --«extend»--> Kiểm tra giỏ hàng"

- **Sai bản chất quan hệ.** Theo Quy tắc nghiệp vụ 1: *"Mọi giao dịch đặt hàng đều BẮT BUỘC phải thực hiện kiểm tra giỏ hàng"*. Một hành vi **bắt buộc luôn xảy ra** khi thực hiện use case chính phải được mô hình bằng **«include»**, không phải «extend» (vốn dùng cho hành vi *tùy chọn*, chỉ chèn vào khi thỏa điều kiện).
- Nếu dùng «extend» ở đây, hệ thống sẽ hiểu sai là "Kiểm tra giỏ hàng" có thể xảy ra hoặc không, dẫn đến rủi ro nghiệp vụ: đơn hàng có thể được tạo mà không qua kiểm tra tồn kho.
- **Sửa:** Đặt hàng ──«include»──> Kiểm tra giỏ hàng (chiều mũi tên giữ nguyên, chỉ đổi nhãn quan hệ).

### Lỗi 2: "Áp dụng mã giảm giá --«include»--> Đặt hàng"

- **Sai cả bản chất quan hệ lẫn chiều mũi tên.**
- Theo Quy tắc nghiệp vụ 2: *"Khách hàng không bắt buộc phải áp dụng mã giảm giá mới đặt được hàng"* → đây là hành vi **tùy chọn**, phải dùng **«extend»**, không phải «include».
- Về chiều mũi tên: nếu dùng «include» thì đúng ra phải là **Use Case chính include Use Case phụ** (A include B nghĩa là A luôn gọi B). Ở đây BA vẽ "Áp dụng mã giảm giá → Đặt hàng", tức coi "Áp dụng mã giảm giá" là use case chính luôn gọi "Đặt hàng" — hoàn toàn ngược với thực tế nghiệp vụ (Đặt hàng mới là use case chính).
- **Sửa đúng theo UML:** Áp dụng mã giảm giá ──«extend»──> Đặt hàng. Chiều mũi tên «extend» xuất phát từ **use case mở rộng (phụ)** trỏ về **use case cơ sở (chính)** — nghĩa là chiều mũi tên giữ nguyên như BA vẽ, nhưng **nhãn quan hệ phải là «extend»** chứ không phải «include». Trên use case "Đặt hàng" cần có thêm **extension point** đánh dấu điểm có thể chèn "Áp dụng mã giảm giá" vào (ví dụ tại bước "trước khi xác nhận thanh toán").

> **Ghi chú về bẫy Voucher hết hạn:** dù voucher hết hạn thì hệ thống báo lỗi nhưng khách vẫn đặt được hàng với giá gốc → càng khẳng định "Áp dụng mã giảm giá" **không bao giờ được là điều kiện bắt buộc** của "Đặt hàng", nên chắc chắn phải dùng «extend», không thể là «include».

## Phần 2 — Sơ đồ Use Case TO-BE

Xem file: `usecase_diagram.drawio` (mở bằng https://app.diagrams.net hoặc draw.io desktop).

**Cấu trúc sơ đồ:**
- Actor: **Khách hàng**
- Use case: Đặt hàng, Kiểm tra giỏ hàng, Áp dụng mã giảm giá
- Quan hệ:
  - Đặt hàng ──«include»──> Kiểm tra giỏ hàng (bắt buộc)
  - Áp dụng mã giảm giá ──«extend»──> Đặt hàng (tùy chọn)
