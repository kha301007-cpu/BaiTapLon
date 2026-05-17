def tinh_loi_nhuan_12_thang(so_tien_goc, lai_suat_nam):
    # Lãi suất theo tháng
    lai_suat_thang = lai_suat_nam / 12
    # Công thức lãi kép: A = P * (1 + r)^n
    so_tien_nhan_duoc = so_tien_goc * ((1 + lai_suat_thang) ** 12)
    loi_nhuan = so_tien_nhan_duoc - so_tien_goc
    return loi_nhuan, so_tien_nhan_duoc