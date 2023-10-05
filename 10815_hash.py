# 숫자 카드
n = int(input())
card = list(map(int, input().split()))
m = int(input())
card_1 = list(map(int, input().split()))

card_dict = {}
for c in card:
    card_dict[c] = 1

for c in card_1:
    print(card_dict.get(c, 0), end = ' ')