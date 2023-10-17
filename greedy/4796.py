# 캠핑
case = 0
answer = []
while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    case += 1
    camping = (v // p) * l
    if (v % p) <= l:
        camping += (v % p)
    else:
        camping += l
    answer.append([case, camping])
for a in answer:
    print(f'Case {a[0]}: {a[1]}')


    
