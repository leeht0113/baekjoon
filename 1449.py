# 수리공 항승
n , l = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
answer = 1
start = data[0] - 0.5
for d in data[1:]:
    end = d + 0.5
    if end - start <= l:
        continue
    else:
        start = d - 0.5
        answer += 1
print(answer)