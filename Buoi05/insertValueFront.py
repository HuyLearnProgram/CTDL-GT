def insertValueFront(inputTuple, valueToInsert):
    return (valueToInsert,) + inputTuple


inputTuple = (2, 3, 4)
valueToInsert = 1
outputTuple = insertValueFront(inputTuple, valueToInsert)
print(outputTuple)
