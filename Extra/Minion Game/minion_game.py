def check_string():
    while (True):
        try:
            string = input('Enter a word: ')
            if string.isalpha() == False:
                raise ValueError
            break
        except ValueError:
            print("Invalid input, try again")
    return string


def find_winner(string):
    length = len(string)
    stuart_points = 0
    kevin_points = 0

    for i in range(length):
        if string[i].lower() in 'aeiou':
            kevin_points += (length - i)
        else:
            stuart_points += (length - i)

    return stuart_points, kevin_points


def output(p1, p2):
    if p1 > p2:
        print("\033[1m" + 'Stuart ' + str(p1) + "\033[0m")
    elif p2 > p1:
        print("\033[1m" + 'Stuart ' + str(p2) + "\033[0m")
    else:
        print("\033[1m" + 'Draw' + "\033[0m")

if __name__ == '__main__':
    word = check_string()
    p1, p2 = find_winner(word)
    output(p1, p2)