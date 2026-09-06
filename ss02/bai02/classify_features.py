def classify_logistics_feature(feature_name):
    """Hàm phân loại tính năng phần mềm vào đúng nhóm TPS, MIS, hoặc DSS."""
    feature_lower = feature_name.lower()
    
    # Ràng buộc: DSS quét trước (bẫy dữ liệu phân tích/dự báo):

    dss_keywords = ["dự báo", "phân tích chiến lược", "mô hình"]
    mis_keywords = ["báo cáo", "thống kê", "tổng hợp"]
    tps_keywords = ["quét mã vạch", "in phiếu", "đã lấy hàng", "bấm nút"]
    
    if any(kw in feature_lower for kw in dss_keywords):
        return "DSS (Hệ thống hỗ trợ quyết định)"
    elif any(kw in feature_lower for kw in mis_keywords):
        return "MIS (Hệ thống thông tin quản lý)"
    elif any(kw in feature_lower for kw in tps_keywords):
        return "TPS (Hệ thống xử lý giao dịch tác nghiệp)"
    else:
        return "Chưa thể phân loại, cần kiểm tra thêm"

if __name__ == "__main__":
    test_features = [
        "Báo cáo tổng hợp doanh thu tháng cho Trưởng bưu cục",
        "Công cụ phân tích dự báo điểm nóng quá tải đơn hàng mùa Tết",
        "Tài xế bấm nút Đã lấy hàng trên App Mobile",
        "Nhân viên kho quét mã vạch nhập kho",
        "In phiếu cước giao hàng cho khách tại bưu cục"
    ]
    
    print("=== Kết Quả Phân loại tự động tính năng===")
    for feature in test_features:
        print(f"Tính năng: {feature}")
        print(f"=> Kết quả: {classify_logistics_feature(feature)}\n")
