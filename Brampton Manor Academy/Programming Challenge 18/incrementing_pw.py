from collections import OrderedDict

def valid_passwords(n):
    result = []
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWQYZ0123456789'
    for letter in alphabet:
        result.append(letter)
    for x in alphabet:
        for y in alphabet:
            if x != y:
                result.append(''.join(sorted(x+y)))

    result = list(OrderedDict.fromkeys(result))

    return result[n-1]


if __name__ == "__main__":
    print(valid_passwords(21))