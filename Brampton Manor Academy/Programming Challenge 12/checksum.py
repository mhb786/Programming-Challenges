def check_card():
    while True:
        try:
            number = input("Enter your card number: ")
            if len(number) != 16:
                raise ValueError
            elif not number.isnumeric():
                raise TypeError
            break
        except ValueError:
            print("Must be 16 digits")
        except TypeError:
            print("Card number must be just numbers")
    return number


def pan(number):
    return f"Personal Account Number (PAN): %s" % number[6:15]


def checksum_digit(number):
    return f"Checksum Digit: %s" % number[-1]


def issuer(number):
    if number[0:2] == "34" or number[0:2] == "37":
        return "Issuer: American Express"
    elif number[0] == "3" and number[0:2] != "34" and number[0:2] != "37":
        return "Issuer: JCB"
    elif number[0] == "4":
        return "Issuer: Visa"
    elif int(number[0:2]) in range(51, 56):
        return "Issuer: MasterCard"


def is_Valid(number):
    digits = list(map(int, number))
    oddSum = sum(digits[-1::-2])
    evnSum = sum([sum(divmod(2 * d, 10)) for d in digits[-2::-2]])
    if (oddSum + evnSum) % 10 == 0:
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    number = check_card()
    print(pan(number))
    print(checksum_digit(number))
    print(issuer(number))
    print(is_Valid(number))