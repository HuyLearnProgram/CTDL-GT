def getDiagonal(inputTuple):
    temp = list()
    for i in range(len(inputTuple)):
        for j in range(len(inputTuple[i])):
            if i == j:
                temp.append(inputTuple[i][j])
    return tuple(temp)


inputTuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
outputTuple = getDiagonal(inputTuple)
print(outputTuple)
