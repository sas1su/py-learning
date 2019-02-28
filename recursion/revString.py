def revString(s):
    #base case
    l = len(s)
    if l == 1:
        return s
    else:
        return revString(s[1:]) + s[0]

s = "Live not on evil"
r = revString(s)
print(s == r)
print(revString(s))