def tops(msg):
    result = ''
    index = 1
    count = 1
    while index < len(msg):
        result += msg[index]
        count += 1
        index = (count**2)*2 - (1*count)
    return result[::-1]

print(tops("abcdefghijklmnopqrstuvwxyz12345"))
