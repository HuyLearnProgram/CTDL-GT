def recursiveMethod(n):
    if n < 1:
        print("n is less than 1")
    else:
        recursiveMethod(n-1)
        print(n)


if __name__ == '__main__':
    recursiveMethod(4)
