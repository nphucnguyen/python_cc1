# lab7.1 check the parenthesis
#input : string S
#ouput: nêu đủ : Success
#       thiếu: vị trí thiếu (bắt đầu từ 1)
#        sai : vị trí sai (bắt đầu từ 1)

from nhap03 import Stack
from nhap03 import StackNode
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
            mark = index +1
        # neu la ]})
        elif paren in ')]}':
            # neu stack het
            if s.isEmpty():
                is_balanced = False
                mark = index +1
            # neu Stack con
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
                    mark = index +1
        index +=1
    if s.isEmpty() and is_balanced:
        return 'Success'
    else:
        return mark
print(is_paren_balanced("foo(bar[i)"))
