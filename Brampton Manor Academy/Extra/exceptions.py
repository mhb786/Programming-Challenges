import operator
ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

def operations():
    table = []
    # inputop = input("Please enter an operator (+, -, *, /): ")
    # inputnum = int(input("Please enter a natural number: "))
    inputop = '+'
    inputnum= int('4')
    for number in range(-1, inputnum+1):
        row = [0]*(inputnum+1)
        table.append([number, row])
    table[0][0] = inputop
    table[0][1] = list(range(inputnum+1))
    for digit in table[2][1]:
        digit = 1000
        return table



print(operations())