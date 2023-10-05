# 숫자 카드
n = int(input())
card = list(map(int, input().split()))
m = int(input())
card_1 = list(map(int, input().split()))
card.sort()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in card_1:
    if binary_search(card, i, 0, n - 1) == None:
        print(0, end= ' ')
    else:
        print(1, end=' ')
