def sumOfDigits(n):
    assert n >= 0 and int(n) == n, 'The number must be positive integer only!'
    if n >= 0 and n < 10:
        return n
    else:
        return n % 10 + sumOfDigits(int(n/10))


if __name__ == '__main__':
    result = sumOfDigits(234)
    print(result)
