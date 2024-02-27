def reverseList(lst):
    for i in range(len(lst)//2):
        lst[i], lst[len(lst)-1-i] = lst[len(lst)-1-i], lst[i]


inp = [1, 2, 3, 4, 5]
reverseList(inp)
print(inp)
