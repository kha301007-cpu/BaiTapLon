def tinh_trung_binh(day_so):
    if not day_so:
        return 0
    return sum(day_so) / len(day_so)