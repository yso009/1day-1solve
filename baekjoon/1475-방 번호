import math
n = str(input())
n = n.replace('9','6') # 9를 6으로 변환
n_c = []
set_n= set(n)

for i in set_n:
    if i == '6':
        n_c.append((math.ceil((n.count(i))/2),i))
    else:
        n_c.append((n.count(i),i))
print(max(n_c)[0])
