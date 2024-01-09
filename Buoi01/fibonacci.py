def fibonacci(n):
    assert n >= 0 and int(
        n) == n, 'Fibonacci number cannot be negative number or non integer.'
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    result = fibonacci(4)
    print(result)
