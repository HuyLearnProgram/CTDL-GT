import array


def daysTemperature():
    tempList = []
    n = int(input("How many day's temperature? "))
    for i in range(n):
        num = int(input("Day "+str(i+1)+"'s high temp: "))
        tempList.append(num)
    tempAvg = sum(tempList)/len(tempList)
    tempCount = sum([1 for el in tempList if el > tempAvg])
    print("Average = "+str(tempAvg))
    print(str(tempCount)+" day(s) above average")


if __name__ == '__main__':
    daysTemperature()
