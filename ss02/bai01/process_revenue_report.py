

def process_revenue_report(order_list):
    total_revenue = 0
    successful_orders = 0
    
    # Xử lý và lọc dữ liệu thô
    for order in order_list:
        if order['status'] == "DELIVERED":
            total_revenue += order['fee']
            successful_orders += 1



            
    # Xử lý ngoại lệ chia cho 0 trong trường hợp không có đơn nào thành công
    avg_revenue = (total_revenue / successful_orders) if successful_orders > 0 else 0



    
    # Xuất thông tin báo cáo điều hành


    print("=== MÀN HÌNH BÁO CÁO DOANH THU ĐIỀU HÀNH ===")
    
    print(f"1. Tổng doanh thu thực tế: {total_revenue:,.0f}đ")
    print(f"2. Số đơn giao thành công: {successful_orders} đơn")
    print(f"3. Doanh thu trung bình/đơn: {avg_revenue:,.0f}đ")
    
    return total_revenue, successful_orders, avg_revenue

if __name__ == "__main__":


    # Dữ liệu thử nghiệm từ máy chủ (Bao gồm bẫy dữ liệu)


    order_data = [
        {"order_id": "01", "fee": 15000, "status": "DELIVERED"},
        {"order_id": "02", "fee": 20000, "status": "DELIVERED"},
        {"order_id": "03", "fee": 0, "status": "CANCELLED"},       # Bỏ qua
        {"order_id": "04", "fee": -5000, "status": "RETURNED"},    # Bỏ qua
        {"order_id": "05", "fee": 25000, "status": "DELIVERED"}
    ]
    
    process_revenue_report(order_data)
