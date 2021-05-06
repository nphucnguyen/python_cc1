from nhap03 import Stack
def is_match(a,b):
    if a == '(' and b == ')':
        return True
    if a == '[' and b == ']':
        return True
    if a == '{' and b == '}':
        return True
    return False
def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0
    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in '([{':
            s.push(paren)
        # neu la ]})
        else:
            if s.isEmpty():
                is_balanced = False
            # neu Stack con
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index +=1
    if s.isEmpty() and is_balanced:
        return True
    else:
        return False
print(is_paren_balanced("()()"))
