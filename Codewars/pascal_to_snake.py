def to_underscore(string):
    if type(string) == int:
        return str(string)
    index = 0
    string = string
    for letter in string[1:]:
        index += 1
        if letter.isupper() == True:
            string = string[:index] + '_' + string[index:]
            index += 1
    return string.lower()


print(to_underscore(1))