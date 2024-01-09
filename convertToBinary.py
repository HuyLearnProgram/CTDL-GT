def convertToBinary(n):
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * convertToBinary(int(n/2))


if __name__ == '__main__':
    print(convertToBinary(13))
