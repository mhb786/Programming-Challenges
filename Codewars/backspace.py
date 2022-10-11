def clean_string(s):
    newstr = ''
    for letter in s.split():
        if letter != '#':
            return newstr.join(letter)

print(clean_string('abc#d##c'))