def reverse(li):
    for i in range(0, int(len(li)/2)):
        other = len(li)-i-1
        temp = li[i]
        li[i] = li[other]
        li[other] = temp
    print(li)


if __name__ == '__main__':
    myList = [1, 2, 3, 4, 5]
    reverse(myList)
