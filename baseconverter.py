from stack import Stack

def baseConverter(decNumber, base):
    # initiate stack to keep the reminder
    hex = "0123456789ABCDEF"
    s = Stack()
    # devide decNumber/2 util it become 0
    # push the rem to stack
    while decNumber > 0:
        rem = decNumber % base
        s.push(rem)
        decNumber = decNumber // base
    # pop stack and append to string
    string = ''
    while not s.isEmpty():
        string = string + hex[s.pop()]
    return string
# main
print(baseConverter(48879, 16))
print(baseConverter(256, 16))
print(baseConverter(25, 8))
print(baseConverter(26, 26))