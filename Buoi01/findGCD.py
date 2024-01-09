def findGCD(a, b):
    if b == 0:
        return a
    else:
        a, b = abs(a), abs(b)
        return findGCD(b, a % b)


if __name__ == '__main__':
    print(findGCD(48, 18))
