def compare_powers(n1,n2):
    if n1[0]**n1[1] > n2[0]**n2[1]:
        return -1
    elif n1[0]**n1[1] == n2[0]**n2[1]:
        return 0
    else:
        return 1

print(compare_powers([2,10],[2,10]))