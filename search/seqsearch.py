def seqSearch(testlist, target):
    pos = 0
    found = False
    while pos < len(testlist) and not found:
        if target == testlist[pos]:
            found = True
        else:
            pos = pos + 1
    return found

testlist = [1, 2, 3, 5, 6]
print(seqSearch(testlist, 1))