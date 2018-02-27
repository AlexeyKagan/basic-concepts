def linear_search(list, item):
    pos = 0
    found = False

    while pos < len(list) and not found:
        if list[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found


testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]

print(linear_search(testlist, 3))
print(linear_search(testlist, 13))
