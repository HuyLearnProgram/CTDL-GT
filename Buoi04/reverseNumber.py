def reverseNumber(num):
    count = len(str(num))-1
    tempNum = 0
    while num != 0:
        subNum = num % 10
        num = int(num/10)
        tempNum += subNum * pow(10, count)
        count -= 1
    return tempNum


print(reverseNumber(123456))
