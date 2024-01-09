def powerOfNumber(num, power):
    if power == 0:
        return 1
    elif power > 0:
        if power % 1 == 0:
            return num * powerOfNumber(num, power-1)
        else:
            return num * powerOfNumber(num, power - 0.5)

    else:
        return 1 / num * powerOfNumber(num, -power-1)


if __name__ == '__main__':
    res = powerOfNumber(2, 4)
    print(res)
