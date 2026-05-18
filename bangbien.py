import pandas as pd

# 1. Định nghĩa dữ liệu dựa trên các hình ảnh thuộc tập dữ liệu UCI
data = {
    "Variable Name": [
        "ID", "X1", "X2", "X3", "X4", "X5", "X6", "X7", "X8", "X9", "X10", "X11",
        "X12", "X13", "X14", "X15", "X16", "X17", "X18", "X19", "X20", "X21", "X22", "X23", "Y"
    ],
    "Role": [
        "ID" if i == 0 else "Target" if i == 24 else "Feature" for i in range(25)
    ],
    "Type": [
        "Binary" if i == 24 else "Integer" for i in range(25)
    ],
    "Demographic": [
        "", " ", "Sex", "Education Level", "Marital Status", "Age", 
        "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""
    ],
    "Description": [
        "Mã định danh khách hàng",
        "LIMIT_BAL (Số tiền tín dụng được cấp)",
        "SEX (1 = Nam, 2 = Nữ)",
        "EDUCATION (1 = Sau ĐH, 2 = ĐH, 3 = Phổ thông, 4 = Khác)",
        "MARRIAGE (Tình trạng hôn nhân)",
        "AGE (Tuổi)",
        "PAY_0 (Lịch sử thanh toán Tháng 9)",
        "PAY_2 (Lịch sử thanh toán Tháng 8)",
        "PAY_3 (Lịch sử thanh toán Tháng 7)",
        "PAY_4 (Lịch sử thanh toán Tháng 6)",
        "PAY_5 (Lịch sử thanh toán Tháng 5)",
        "PAY_6 (Lịch sử thanh toán Tháng 4)",
        "BILL_AMT1 (Số tiền hóa đơn Tháng 9)",
        "BILL_AMT2 (Số tiền hóa đơn Tháng 8)",
        "BILL_AMT3 (Số tiền hóa đơn Tháng 7)",
        "BILL_AMT4 (Số tiền hóa đơn Tháng 6)",
        "BILL_AMT5 (Số tiền hóa đơn Tháng 5)",
        "BILL_AMT6 (Số tiền hóa đơn Tháng 4)",
        "PAY_AMT1 (Số tiền đã trả Tháng 9)",
        "PAY_AMT2 (Số tiền đã trả Tháng 8)",
        "PAY_AMT3 (Số tiền đã trả Tháng 7)",
        "PAY_AMT4 (Số tiền đã trả Tháng 6)",
        "PAY_AMT5 (Số tiền đã trả Tháng 5)",
        "PAY_AMT6 (Số tiền đã trả Tháng 4)",
        "default payment next month (Khách hàng quỵt nợ/vi phạm: 1=Có, 0=Không)"
    ],
    "Units": [""] * 25,
    "Missing Values": ["no"] * 25
}

