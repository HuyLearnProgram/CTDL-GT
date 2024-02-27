def tupleElementwiseSum(tuple1, tuple2):
    temp = list()
    for i in range(len(tuple1)):
        temp.append(tuple1[i] + tuple2[i])
    return tuple(temp)


tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
outputTuple = tupleElementwiseSum(tuple1, tuple2)
print(outputTuple)
