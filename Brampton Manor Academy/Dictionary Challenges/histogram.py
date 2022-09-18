word = str(input('Enter word: '))

def check_freq(word):
    freq = {}
    for letter in set(word):
       freq[letter] = word.count(letter)
    return freq

print(check_freq(word))
