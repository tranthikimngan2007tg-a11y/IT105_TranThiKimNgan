# Bài 2: Thực hành Phân tích và khảo sát toàn diện hệ thống ngân hàng số RikkeiBank

## Bước 1: Nhận diện 5 thành phần HTTT và phân biệt Dữ liệu vs Thông tin

### 1.1. Bảng 5 thành phần HTTT

| Thành phần HTTT | Ví dụ thực tế tại RikkeiBank | Vai trò cơ bản |
|---|---|---|
| 1. Phần cứng (Hardware) | Máy chủ xử lý giao dịch Core Banking, máy ATM/POS | Hạ tầng vật lý xử lý và giao tiếp tài chính |
| 2. Phần mềm (Software) | Ứng dụng RikkeiBank Mobile, hệ thống Internet Banking | Giao diện và logic thực hiện giao dịch số |
| 3. Dữ liệu (Data) | Số dư tài khoản, lịch sử biến động số dư | Dữ liệu tài chính cốt lõi |
| 4. Con người (People) | Khách hàng cá nhân sử dụng ứng dụng, Giao dịch viên tại quầy | Tác nhân trực tiếp tương tác với hệ thống |
| 5. Quy trình (Process) | Quy trình chuyển khoản: đăng nhập → nhập thông tin thụ hưởng → xác thực OTP/sinh trắc học → xác nhận giao dịch | Trình tự các bước xác thực và chuyển khoản |

### 1.2. Bảng phân loại Dữ liệu vs Thông tin

| STT | Nội dung dữ liệu tại RikkeiBank | Dữ liệu (Data) | Thông tin (Information) | Lý do phân loại |
|---|---|---|---|---|
| 1 | 50000000 | [x] | [ ] | Chuỗi số thô, chưa rõ là tiền gửi, tiền vay hay hạn mức |
| 2 | Khách hàng Trần Văn C chuyển 5.000.000 VNĐ lúc 10:15 ngày 15/08 | [ ] | [x] | Đầy đủ ngữ cảnh giao dịch: Ai, Số tiền, Thời gian |
| 3 | 0987654321 | [x] | [ ] | Chuỗi số thô, có thể là số điện thoại hoặc số tài khoản |
| 4 | Tổng số dư tiết kiệm trực tuyến của chi nhánh đạt 200 tỷ VNĐ trong tháng 8 | [ ] | [x] | Đã có ngữ cảnh: khoản mục (tiết kiệm trực tuyến), đơn vị tiền tệ, phạm vi (chi nhánh) và mốc thời gian (tháng 8) → có ý nghĩa hỗ trợ ra quyết định |
| 5 | TK101, Nguyễn Thị D, Active, Gold | [ ] | [x] | Chuỗi ký tự đã gắn với một khách hàng cụ thể (mã tài khoản, họ tên, trạng thái, hạng thẻ) → đủ ngữ cảnh để nhận diện một hồ sơ tài khoản |

---

## Bước 2: Khảo sát môi trường và xác định Stakeholders

### 2.1. Bảng phân loại môi trường

| Yếu tố khảo sát tại RikkeiBank | Thuộc loại môi trường | Tầm ảnh hưởng đến hệ thống |
|---|---|---|
| Năng lực bảo mật của đội ngũ IT | Môi trường Nội bộ | Quyết định khả năng phòng chống tấn công mạng |
| Thông tư an toàn thông tin Ngân hàng Nhà nước | Môi trường Bên ngoài | Quy định bắt buộc về xác thực sinh trắc học |
| Hệ thống đường truyền liên ngân hàng Napas | Môi trường Bên ngoài | Ảnh hưởng trực tiếp đến tốc độ chuyển tiền liên ngân hàng |
| Thói quen sử dụng điện thoại của người cao tuổi | Môi trường Bên ngoài | Đòi hỏi giao diện đơn giản, chữ to, ít bước thao tác để nhóm khách hàng lớn tuổi dễ sử dụng |
| Chính sách lãi suất của các ngân hàng đối thủ | Môi trường Bên ngoài | Tạo áp lực cạnh tranh, buộc hệ thống phải bổ sung tính năng/ưu đãi để giữ chân khách hàng |

### 2.2. Bảng Stakeholders

| Nhóm Stakeholder | Vai trò trong dự án | Mối quan tâm lớn nhất đối với phần mềm |
|---|---|---|
| 1. Khách hàng cá nhân | Người dùng dịch vụ cuối | Chuyển tiền nhanh chóng, an toàn, giao diện mượt mà |
| 2. Chuyên viên An ninh mạng | Giám sát bảo mật | Hệ thống chống rò rỉ mã OTP và mã hóa dữ liệu đầu cuối |
| 3. Giao dịch viên tại quầy | Người vận hành trực tiếp (người dùng nghiệp vụ) | Thao tác xử lý giao dịch nhanh, chính xác, hạn chế sai sót khi hỗ trợ khách hàng tại quầy |

---

## Bước 3: Lựa chọn kỹ thuật thu thập yêu cầu và soạn câu hỏi mẫu

### 3.1. Bảng lựa chọn kỹ thuật

| STT | Tình huống khảo sát tại RikkeiBank | Kỹ thuật phù hợp nhất | Lý do lựa chọn ngắn gọn |
|---|---|---|---|
| 1 | Khảo sát nhu cầu giao dịch của 50.000 khách hàng trẻ Gen Z | Bảng câu hỏi / Khảo sát (Survey) | Quy mô người dùng cực lớn, thu thập nhanh số liệu định lượng |
| 2 | Làm rõ quy định đối soát và hạn mức chuyển khoản với Giám đốc rủi ro | Phỏng vấn (Interview) | Chuyên gia cấp cao, cần trao đổi sâu về chính sách nghiệp vụ |
| 3 | Xem thực tế thao tác nhập lệnh chuyển tiền quốc tế của giao dịch viên | Quan sát (Observation) | Cần theo dõi trực tiếp thao tác thực tế trên hệ thống, phát hiện các bước hoặc khó khăn không thể hiện được qua mô tả bằng lời |
| 4 | Đọc các văn bản hướng dẫn tiêu chuẩn bảo mật thanh toán PCI-DSS | Nghiên cứu tài liệu (Document Analysis) | Tiêu chuẩn quốc tế dạng văn bản quy chuẩn có sẵn |
| 5 | Lấy ý kiến đóng góp của nhóm 15 chuyên viên chăm sóc khách hàng VIP | Phỏng vấn nhóm nhỏ / Workshop (Focus Group) | Số lượng vừa phải, cần trao đổi để thảo luận và thống nhất ý kiến đóng góp mang tính chuyên sâu, khó lượng hóa bằng survey |

### 3.2. Câu hỏi trắc nghiệm khảo sát khách hàng cá nhân

**Câu hỏi:** "Khi chuyển tiền trên ứng dụng RikkeiBank, yếu tố nào quan trọng nhất với bạn?"

- A. Tốc độ xử lý giao dịch nhanh chóng
- B. Mức độ bảo mật và an toàn khi xác thực giao dịch
- C. Không mất phí hoặc phí giao dịch thấp
- D. Giao diện đơn giản, dễ thao tác

---

## Bước 4: Phân loại Yêu cầu Chức năng (FR) và Phi chức năng (NFR)

| STT | Phát biểu yêu cầu | Phân loại (FR / NFR) | Mã định danh đề xuất | Câu hỏi cốt lõi giải thích |
|---|---|---|---|---|
| (1) | Khách hàng có thể quét mã QR để thanh toán hóa đơn | FR | FR-01 | Hành động hệ thống cung cấp (LÀM GÌ) |
| (2) | Giao dịch chuyển tiền phải hoàn tất trong vòng dưới 3 giây | NFR | NFR-01 | Tiêu chuẩn tốc độ xử lý (TỐT NHƯ THẾ NÀO) |
| (3) | Mọi giao dịch trên 10 triệu VNĐ bắt buộc xác thực sinh trắc học khuôn mặt | NFR | NFR-02 | Tiêu chuẩn an ninh và bảo mật (TỐT NHƯ THẾ NÀO) |
| (4) | Khách hàng có thể mở sổ tiết kiệm trực tuyến ngay trên ứng dụng | FR | FR-02 | Hành động hệ thống cung cấp (LÀM GÌ) |
| (5) | Hệ thống Core Banking chịu tải được 10.000 giao dịch đồng thời mỗi giây | NFR | NFR-03 | Tiêu chuẩn về khả năng chịu tải/mở rộng (scalability): hệ thống vận hành TỐT NHƯ THẾ NÀO dưới áp lực lớn |

---

## Bước 5: Đặc tả User Story chuẩn ba thành phần

**User Story dành cho Khách hàng chuyển tiền:**

| Thành phần User Story | Nội dung |
|---|---|
| Là một (Vai trò - Who) | Khách hàng sử dụng ứng dụng RikkeiBank |
| Tôi muốn (Hành động - What) | Lưu danh bạ người thụ hưởng thường xuyên chuyển tiền |
| Để (Lợi ích - Why) | Không phải nhập lại thông tin tài khoản mỗi lần chuyển tiền, tiết kiệm thời gian và giảm rủi ro nhập sai số tài khoản thụ hưởng |

> **User Story hoàn chỉnh:** "Là một Khách hàng sử dụng ứng dụng RikkeiBank, tôi muốn lưu danh bạ người thụ hưởng thường xuyên chuyển tiền, để không phải nhập lại thông tin mỗi lần và giảm rủi ro nhập sai số tài khoản."
