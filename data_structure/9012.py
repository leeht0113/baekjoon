# 괄호
import sys
input = sys.stdin.readline
answer = []
for _ in range(int(input())):
    parenthesis = input()
    stack = []
    isVPS = 'YES'
    for p in parenthesis:
        if p == '(':
            stack.append(p)
        elif p == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                isVPS = 'NO'
                break
    if stack:
        isVPS = 'NO'
    answer.append(isVPS)
for a in answer:
    print(a)