import re

brackets = {')': '(', '}': '{', ']': '['}
stack = []
for s in ['( ){[ 1 ]( 1 + 3 )( ){ }}', '( 23 ( 2 - 3);', '( 11 }']:
    result = re.sub(r'[^\[\]\(\)\{\}]', '', s)
    for char in result:
        if char in brackets and stack[-1] == brackets[char]:
            stack.pop()
        elif char not in brackets:
            stack.append(char)
        else:
            break

    print(f'{s} {'Симетрично' if len(stack) == 0 else 'Несиметрично'}')