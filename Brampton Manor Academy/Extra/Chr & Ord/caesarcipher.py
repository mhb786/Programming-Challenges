def encrypt(text, key):

    def shift(x):
        if not x.isalpha():
            return x
        result = ord(x)+key
        if x.isupper() and result > 90:
            result -= 26
        elif x.islower() and result > 122:
            result -= 26
        return chr(result)

    return ''.join(list(map(shift, text)))


def decrypt(text, key):

    def shift(x):
        if not x.isalpha():
            return x
        result = ord(x) - key
        if x.isupper() and result < 65:
            result += 26
        elif x.islower() and result < 97:
            result += 26
        return chr(result)

    return ''.join(list(map(shift, text)))


def brute(text):
    for x in range(1, 27):
        print(x, decrypt(text, x))


if __name__ == "__main__":
    choice = input("Do you wish to encrypt or decrypt or brute force a message?: ")
    message = input("Enter your message: ")

    if choice == "encrypt":
        key = int(input("Enter your key number(1-26): "))
        print("Your translated text is: %s" % encrypt(message, key))
    elif choice == "decrypt":
        key = int(input("Enter your key number(1-26): "))
        print("Your translated text is: %s" % decrypt(message, key))
    elif choice == "brute":
        brute(message)
