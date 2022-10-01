def snail(map):
    newmap = []
    while (map):
        newmap.append(map.pop(0))
        map = list(map(list, zip(*)))

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

print(snail(array))