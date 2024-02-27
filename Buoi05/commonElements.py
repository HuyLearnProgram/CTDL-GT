def commonElements(tuple1, tuple2):
    temp = list()
    for i in tuple1:
        if i in tuple2:
            temp.append(i)
    return tuple(temp)


tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
outputTuple = commonElements(tuple1, tuple2)
print(outputTuple)
