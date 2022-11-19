word = str(input('Enter word: '))

def histogram(string):
    all_freq = {}
    for i in string:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    return all_freq


print(histogram(word))
