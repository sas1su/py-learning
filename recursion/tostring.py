def toStr(n, base):
    #base case
    convString = '0123456789ABCDF'
    if n < base:
        return convString[n]
    else:
        return toStr(n//base, base) + convString[n%base]

print(toStr(769, 2)) 