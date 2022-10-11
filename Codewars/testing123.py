def number(lines):
    list = []
    order = 1
    for line in lines:
        list.append(f"{order}: {line}")
        order += 1
    return list

print(number(["a", "b", "c"]))