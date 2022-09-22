def rome_to_int(x):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
    num = 0
    last = 'I'

    for numeral in x[::-1]:
        if roman_numerals[numeral] < roman_numerals[last]:
            num -= roman_numerals[numeral]
        else:
            num += roman_numerals[numeral]
        last = numeral
    return num


def int_to_rome(x):
    numbers = [1,4,5,9,10,40,50,90,100]
    roman = ['I','IV','V','IX','X','XL','L','XC','C']
    i = 8
    roman_numeral = ''
    while x != 0:
        if numbers[i] <= x:
            roman_numeral += roman[i]
            x = x - numbers[i]
        else:
            i -= 1
    return roman_numeral

firstnum = str(input('Enter First Roman Number (no spaces): '))
print(f'Value of {firstnum}: {rome_to_int(firstnum)}')

secondnum = str(input('Enter Second Roman Number (no spaces): '))
print(f'Value of {secondnum}: {rome_to_int(secondnum)}')

digital_sum = rome_to_int(firstnum) + rome_to_int(secondnum)
print(f'Digital sum is {digital_sum}')

print(f'Roman sum is {int_to_rome(digital_sum)}')


