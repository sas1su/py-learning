def ordSeqSearch(alist, item):
    pos   = 0
    found = False
    stop  = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            # no point continuing if item in the list is > list to found: STOP
            if item < alist[pos]:
                stop = True
            pos = pos + 1
    return found


testlist = [1, 9, 13, 22, 27, 29]
print(ordSeqSearch(testlist, 13))
print(ordSeqSearch(testlist, 3))