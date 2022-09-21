def obtener_fracciones(frac_str):
    if isinstance(frac_str, (int, float)):
        return frac_str

    if "/" in frac_str:
        try:
            return float(frac_str)
        except ValueError:
            num, denom = frac_str.split("/")
            try:
                leading, num = num.split(" ")
                whole = float(leading)
            except ValueError:
                whole = 0
            frac = float(num) / float(denom)
            return whole - frac if whole < 0 else whole + frac
    return float(frac_str)
