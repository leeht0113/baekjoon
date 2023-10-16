# 외계인의 기타 연주
import sys
input = sys.stdin.readline
n, p = map(int, input().split())
melody = [list(map(int, input().split())) for _ in range(n)]

count = 0
temp = {}
for i in range(1, 7):
    temp[i] = []
for string, fret in melody:
    fret_list = temp[string]
    if len(fret_list) > 0:
        l = fret_list[-1]
        if fret > l:
            temp[string].append(fret)
            count += 1
        elif fret == l:
            continue
        elif fret < l:
            while temp[string]:
                temp_l = temp[string][-1]
                if fret < temp_l:
                    temp[string].pop()
                    count += 1
                else:
                    break
            if len(temp[string]) > 0:
                if fret != temp[string][-1]:
                    temp[string].append(fret)
                else:
                    continue
            elif len(temp[string]) == 0:
                temp[string].append(fret)
            count += 1
    else:
        temp[string].append(fret)
        count += 1
print(count)