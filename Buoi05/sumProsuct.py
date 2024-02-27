def sumProduct(inputTuple):
    sum, product = 0, 1
    for i in inputTuple:
        sum += i
        product *= i
    return sum, product


inputTuple = (1, 2, 3, 4)
sumResult, productResult = sumProduct(inputTuple)
print(sumResult, productResult)
