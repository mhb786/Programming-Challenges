def encrypter(n, word):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dial = ''
    count = 26 % n

    while len(alphabet) > n:
        for x in (alphabet[n-count:]+alphabet[:n-count])[::n]:
            dial += x
            alphabet = alphabet.replace(x, '')
        alphabet = alphabet[n-(count+1):]+alphabet[:n-(count+1)]


if __name__ == "__main__":
    print(encrypter(5, 'ABCD'))