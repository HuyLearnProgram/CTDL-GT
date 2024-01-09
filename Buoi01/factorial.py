def factorial(n):
    assert n >= 0 and int(n) == n, 'The number must be positive integer only!'
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n-1)


if __name__ == '__main__':
    result = factorial(3)
    print(result)
