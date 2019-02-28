import stack
# symbols = ()
# push to stack if opening (
# pop from stack if closing )
# stack empty is True
def parParser(symbols):
    myStack = stack.Stack()
    changed = True
    i = 0
    while i < len(symbols) and changed:
        if symbols[i] in '([{':
            myStack.push(symbols[i])
        else:
            if myStack.isEmpty():
                changed = False
            else:
                start = myStack.pop()
                if not matches(start, symbols[i]):
                    changed = False

        i = i + 1

    if myStack.isEmpty() and changed:
        return True
    else:
        return False

def matches(start, close):
    opening = '([{'
    closure = ')]}'
    return opening.index(start) == closure.index(close)


print(parParser('()[]{}'))
print(parParser('(()[]{})'))
print(parParser('(([]]{}}))'))