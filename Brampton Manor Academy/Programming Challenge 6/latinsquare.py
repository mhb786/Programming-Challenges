order = int(input("Enter order of sq: "))
top_left = int(input("Enter top left number: "))

leftnum = 0

leftnum += top_left
numinline = 0

def latinsquare(top_left, leftnum, numinline):
    for values in range(1, order + 1):
        while numinline != order:
            print(top_left, end=" ")
            top_left += 1
            numinline += 1
            if top_left == order + 1:
                top_left = 1
        print()

        numinline = 0
        leftnum += 1
        if leftnum == order + 1:
            leftnum = 1
            top_left = leftnum
        else:
            top_left = leftnum

latinsquare(top_left, leftnum, numinline)