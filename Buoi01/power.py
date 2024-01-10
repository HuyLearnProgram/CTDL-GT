import math


def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent > 0:
        if exponent % 1 == 0:
            return base * power(base, exponent-1)
        else:
            return float_pow(base, exponent)
    else:
        if exponent % 1 == 0:
            return 1 / base * power(base, exponent+1)
        else:
            return float_pow(base, exponent)


def float_pow(v, w, z=None):
    iv = float(v)
    iw = float(w)
    ix = 0.0
    negate_result = 0

    # Kiểm tra xem có tham số thứ ba hay không
    if z is not None:
        raise TypeError(
            "pow() 3rd argument not allowed unless all arguments are integers")

    # Xử lý các trường hợp đặc biệt
    if iw == 0:
        return 1.0
    # Kiểm tra số và mũ có phải là số hay không
    if math.isnan(iv):
        return iv
    if math.isnan(iw):
        return 1.0 if iv == 1.0 else iw
    # Xử lý trường hợp số mũ (exponent) là vô cùng
    if math.isinf(iw):
        iv = abs(iv)
        # Trường hợp 1.0 ** inf luôn là 1.0
        if iv == 1.0:
            return 1.0
        # Trường hợp cả cơ số (base) và số mũ (exponent) cùng hường vô cùng (cả hai cùng dương hoặc cùng âm)
        elif (iw > 0.0) == (iv > 1.0):
            return abs(iw)
        # Trường hợp một dương một âm
        else:
            return 0.0

    # Xử lý trường hợp cơ số (base) vô cùng
    if math.isinf(iv):
        iw_is_odd = iw % 2 != 0
        if iw > 0.0:
            return iw if iw_is_odd else abs(iv)
        else:
            return iw if iw_is_odd else 0.0
    # Xử lý trường hợp cơ số (base) = 0.0
    if iv == 0.0:
        iw_is_odd = iw % 2 != 0
        # Trường hợp 0.0 mũ âm (điều này không xác định và gây lỗi)
        if iw < 0.0:
            raise ZeroDivisionError("0.0 cannot be raised to a negative power")
        return iv if iw_is_odd else 0.0

    if iv < 0.0:
        # if iw != int(iw):
        #     return complex_pow(v, w, z)
        iv = -iv
        negate_result = iw % 2 != 0

    if iv == 1.0:
        return -1.0 if negate_result else 1.0

    try:
        ix = pow(iv, iw)
    except OverflowError:
        raise OverflowError("math range error")

    if negate_result:
        ix = -ix

    return ix


if __name__ == '__main__':
    res = power(2, -1.4)
    print(pow(2, -1.4))
    print(res)
