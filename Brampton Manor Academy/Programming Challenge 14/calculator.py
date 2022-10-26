ops = {'+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '*': lambda x, y: x * y,
      '/': lambda x, y: x / y,
      '//': lambda x, y: x // y,
      '%': lambda x, y: x % y,
      '**': lambda x, y: x ** y}

def calculator():
    while True:
        expression = input("Enter your calculation: ")
        num1, num2, op = expression.split()

        print(ops[op](int(num1), int(num2)))


if __name__ == "__main__":
    calculator()