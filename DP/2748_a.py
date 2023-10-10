# 피보나치 수 2
# top down
cache = [-1] * 91
cache[0] = 0
cache[1] = 1
cnt = 0

def f(n):
    global cnt

    cnt += 1

    if cache[n] == -1:
        cache[n] = f(n - 1) + f(n - 2)

    return cache[n]

    # if n == 0:
    #     return 0
    # elif n == 1:
    #     return 1
    # return f(n - 1) + f(n - 2)

    

print(f(int(input())))
# print(f'cnt: {cnt}')

# 반복문
# bottom up
# N = int(input())
# cache = [-1] * 91
# cache[0] = 0
# cache[1] = 1

# for i in range(2, N + 1):
#     cache[i] = cache[i - 1] + cache[i - 2]

# print(cache[N])