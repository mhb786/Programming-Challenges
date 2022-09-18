word = str(input('Enter word: '))

def histogram(word):
    hist = {}
    for letter in set(word):
       hist[letter] = word.count(letter)
    return hist

print(histogram(word))
