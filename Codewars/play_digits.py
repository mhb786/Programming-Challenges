def dig_pow(n, p):
    result = 0
    for num in str(n):
        result += int(num) ** p
        p += 1
    return p/n if p%n==0 else -1

print(dig_pow(695, 2))