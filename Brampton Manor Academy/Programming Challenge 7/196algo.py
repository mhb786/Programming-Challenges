bottomNum = int(input("Integer 1: "))
topNum = int(input("Integer 2: "))

def palindrome():
    pal_count = 0
    non_lychrel_count = 0
    lychrel_count = 0
    for num in range(int(bottomNum),int(topNum)+1):
        number = str(num)
        revNum = number[::-1]
        count = 0
        while number != revNum and count <= 60:
            number = str(int(number) + int(revNum))
            revNum = number[::-1]
            count += 1
        if count > 60:
            print(num,'is probably lychrel')
            lychrel_count += 1
        elif count == 0:
            pal_count += 1
        else:
            non_lychrel_count += 1
    print()
    print('Palindrome Number Count:', pal_count)
    print('Non-Lychrel Number Count:', non_lychrel_count)
    print('Lychrel Count:', lychrel_count)

palindrome()

