if __name__ == "__main__":
    print("--- KẾT QUẢ THỰC HÀNH CODE PYTHON ---")
    
    # Thử nghiệm Ý 3.1: Giai thừa
    n = 5
    print(f"1. Giai thừa của {n} là: {tinh_giai_thua(n)}")
    
    # Thử nghiệm Ý 3.2: Trung bình dãy số
    day_so = [10, 20, 30, 40, 50]
    print(f"2. Giá trị trung bình của dãy số {day_so} là: {tinh_trung_binh(day_so)}")
    
    # Thử nghiệm Ý 3.3: Tính lợi nhuận (Ví dụ: Gốc 100 triệu, lãi suất 6%/năm)
    goc = 100000000  # 100,000,000 VND
    lai_suat = 0.06  # 6%
    loi_nhuan, tong_tien = tinh_loi_nhuan_12_thang(goc, lai_suat)
    print(f"3. Gửi tiết kiệm {goc:,} VND với lãi suất {lai_suat*100}%/năm:")
    print(f"   - Tiền lợi nhuận sau 12 tháng: {loi_nhuan:,.2f} VND")
    print(f"   - Tổng số tiền nhận được: {tong_tien:,.2f} VND")