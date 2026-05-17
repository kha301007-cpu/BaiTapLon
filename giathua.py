def tinh_giai_thua(n):
    if n < 0:
        return "Không tính được giai thừa cho số âm."
    elif n == 0 or n == 1:
        return 1
    else:
        ket_qua = 1
        for i in range(2, n + 1):
            ket_qua *= i
        return ket_qua
    