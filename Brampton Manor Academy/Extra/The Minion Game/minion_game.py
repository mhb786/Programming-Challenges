from time import sleep

def check_string():
    while True:
        try:
            string = input('Enter a word: ')
            if string.isalpha() == False:
                raise ValueError
            break
        except ValueError:
            sleep(1)
            print("Invalid input, try again")
    return string


def find_winner(string):
    length = len(string)
    p1 = 0
    p2 = 0

    for count, value in enumerate(string):
        if value.lower() in 'aeiou':
            p2 += (length - count)
        else:
            p1 += (length - count)

    return p1, p2


def output(p1, p2):
    print("Calculating...")
    sleep(2)
    if p1 > p2:
        print("\033[1m" + 'Stuart ' + str(p1) + "\033[0m")
    elif p2 > p1:
        print("\033[1m" + 'Kevin ' + str(p2) + "\033[0m")
    else:
        print("\033[1m" + 'Draw' + "\033[0m")


if __name__ == '__main__':
    word = check_string()
    p1, p2 = find_winner(word)
    output(p1, p2)