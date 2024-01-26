def foo(li):
    product = 1
    for i in li:
        product *= i
    print("Sum = "+str(sum(li))+", Product = "+str(product))


if __name__ == '__main__':
    myList = [1, 2, 3, 4, 5]
    foo(myList)
