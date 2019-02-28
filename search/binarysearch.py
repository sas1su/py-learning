def binarySearch(alist, item):
    first = 0
    last  = len(alist) - 1
    found = False
    while  first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        elif alist[midpoint] < item:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return found

def recBinarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        mid = len(alist) // 2
        if alist[mid] == item:
            return True
        else:
            if alist[mid] < item:
                return recBinarySearch(alist[mid+1:], item)
            else:
                return recBinarySearch(alist[:mid-1], item)

testlist = [1, 3, 10, 20, 32, 44, 54, 56, 65, 90]
print(binarySearch(testlist, 54))
print(binarySearch(testlist, 55))

print(recBinarySearch(testlist, 22))
