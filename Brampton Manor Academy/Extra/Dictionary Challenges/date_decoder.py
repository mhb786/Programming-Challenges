months = {
    'JAN': 1, 'FEB': 2, 'MAR': 3, 'APR': 4, 'MAY': 5, 'JUN': 6,
    'JUL': 7, 'AUG': 8, 'SEP': 9, 'OCT': 10, 'NOV': 11, 'DEC': 12
}

date = input('Enter date in the format \'dd-mmm-yy\': ')

def splitdate(date, months):
    split = date.split('-')
    print(f'{split[0]}, {str(months[split[1]])}, {split[2]}')

splitdate(date, months)

