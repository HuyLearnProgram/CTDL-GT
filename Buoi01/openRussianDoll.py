def openRussianDoll(doll):
    if doll == 1:
        print("All dolls are opened")
    else:
        openRussianDoll(doll-1)


if __name__ == '__main__':
    openRussianDoll(3)
