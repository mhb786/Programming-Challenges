def find_missing_digit(isbn):
    result = 0
    isbn = list(isbn)

    # result += ((10*count) if x == 'X' else (int(x)*count) for count, x in enumerate(isbn[::-1], 1))
    for count, x in enumerate(isbn[::-1], 1):
        if x == 'X':
            result += 10 * count
        else:
            result += int(x) * count

    missing = (11 * round(result/11)) - result

    if missing < 0:
        missing += 11
    if missing == 10:
        missing = 'X'

    return missing


if __name__ == "__main__":
    print(find_missing_digit('15688?111X'))