def searchTuple(pTuple, element):
    for i in range(0, len(pTuple)):
        if pTuple[i] == element:
            return f"The {element} is found at {i} index"
    return 'The element is not found'


newTupple = ('a', 'b', 'c', 'd', 'e')
# print(newTupple[1])
# print(newTupple[-1])
# print(newTupple[-2])
# print(newTupple[1:3])
# print(newTupple[:3])
# print(newTupple[1:])
# print(newTupple[:])
# Traverse through Tuple
# for i in newTupple:
#     print(i)
# for i in range(len(newTupple)):
#     print(newTupple[i])
# print('a' in newTupple)
# print(newTupple.index('c'))
# print(searchTuple(newTupple, 'b'))

myTuple = (1, 4, 3, 2, 5)
myTuple1 = (1, 2, 6, 9, 8, 7)
# print(myTuple+myTuple1)
# print(myTuple*4)
# print(myTuple.count(2))
# print(tuple([1, 2, 3, 4]))
list1 = [(1, 2), (9, 0), (3, 4)]
tuple1 = ([1, 2], [3, 4], [5, 6])
print(list1)
print(tuple1)
