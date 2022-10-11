def increment_string(string):
    if string[-1].isdigit() == False:
        return string + '1'
    else:
        newstring = ''
        for letter in string[::-1]:
            if letter.isdigit() == True:
                newstring.join(letter)
            return newstring



print(increment_string('foobar987'))