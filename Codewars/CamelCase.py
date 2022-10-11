def camel_case(string):
    string = string.title()
    string = string.replace(" ", "")
    return string

print(camel_case('hello world'))