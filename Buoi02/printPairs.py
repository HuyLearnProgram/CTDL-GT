import array


def printPairs(array):
    for i in array:
        for j in array:
            print(str(i)+","+str(j))


if __name__ == '__main__':
    my_array = array.array('i', [1, 2, 3, 4, 5])
    printPairs(my_array)
