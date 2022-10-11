def find_outlier(integers):
    odds = []
    evens = []
    for num in integers:
        if num%2==0:
            evens.append(num)
        else:
            odds.append(num)
    if len(odds) > len(evens):
        return evens[0]
    else:
        return odds[0]

print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
