import itertools

def arrangement(array, n):
    array = [int(x) for x in array]
    total = ['A'*array[0], 'B'*array[1], 'C'*array[2], 'D'*array[3]]
    total = ''.join(x for x in total if x.strip())

    result = sorted(set(itertools.permutations(total)))

    return ''.join(result[n-1])


if __name__ == "__main__":
    array = list(input("Enter 4 values: "))
    n = int(input("Enter the nth combination you want: "))

    print(arrangement(array, n))