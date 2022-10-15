import operator
ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

def operations():
    table = []
    inputop = input("Please enter an operator (+, -, *, /): ")
    inputnum = int(input("Please enter a natural number: "))
    for number in range(-1, inputnum+1):
        row = [0]*(inputnum+1)
        table.append([number, row])
    table[0][0] = inputop
    table[0][1] = list(range(inputnum+1))
    index = 0
    topnum = 0
    n = 1
    while n <= inputnum+1:
        while topnum < inputnum+1 and index < inputnum+1:
            try:
                table[n][1][index] = ops[inputop](table[n][0], table[0][1][topnum])
            except:
                table[n][1][index] = '-'
            index+=1
            topnum+=1
        index = 0
        topnum = 0
        n+=1
    for x in table:
        x.insert(1, ' | ')
    table.insert(1, '------------------')
    for row in table:
        print(*row)



print(operations())
