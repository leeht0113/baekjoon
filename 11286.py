# 절댓값 힙

import heapq
import sys

input = sys.stdin.readline
n = int(input())
absolute_heap = []

for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(absolute_heap, (abs(x), x))
    else:
        if absolute_heap:
            print(heapq.heappop(absolute_heap)[1])
        else:
            print(0)