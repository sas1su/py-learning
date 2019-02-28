import stack

def revstr(s):
    mystack = stack.Stack()
    for ch in s:
        mystack.push(ch)

    st = ''
    while not mystack.isEmpty():
        st = st + mystack.pop()
    return st

def main():
    print(revstr("sumesh"))
main()