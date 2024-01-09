def powerOfTwo(n):
    if n == 0:
        return 1
    else:
        power = powerOfTwo(n-1)
        return power * 2


if __name__ == '__main__':
    result = powerOfTwo(4)
    print(result)
