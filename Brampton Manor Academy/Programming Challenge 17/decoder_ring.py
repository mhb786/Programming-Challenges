def encrypter(n, word):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dial = ''
    count = n - 1

    while len(alphabet) > 0:
        for x in (alphabet[count:]+alphabet[:count])[::n]:
            dial += x
            count = alphabet.index(x) - 1
            alphabet = alphabet.replace(x, '')
        count += n
    print(dial)

    result = ''
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    index = 0
    for letter in word:
        count = alphabet.index(letter) + index
        if count+1 > 26:
            count -= 26
        result += dial[count]
        index += 1
        
    return result


if __name__ == "__main__":
    print(encrypter(10, 'MZNOYW'))
