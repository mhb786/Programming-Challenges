def delete_nth(list, max):
    result = []
    for digit in list:
        if digit not in result or result.count(digit) < max:
            result.append(digit)
    return result


print(delete_nth([1,1,3,3,7,2,2,2,2], 3))

