import array


def daysTemperature():
    tempArray = array.array('i')
    tempSum = 0
    n = int(input("How many day's temperature? "))
    for i in range(n):
        num = int(input("Day "+str(i+1)+"'s high temp: "))
        tempSum += num
        tempArray.insert(1, num)
    tempAvg = tempSum/len(tempArray)
    count = 0
    for el in tempArray:
        if el > tempAvg:
            count += 1
    print("Average = "+str(tempAvg))
    print(str(count)+" day(s) above average")


if __name__ == '__main__':
    daysTemperature()
