from math import ceil
a,b,c = list(map(int, input().split()))

if b > c : b,c = c,b

print(b,c)
count = 1

while True:

    if b%2 == 1 and c - b == 1 : 
        print(count)
        break

    else:
        a = round(a / 2)
        count = count + 1

        if b%2 == 1: b = ceil(b/2)
        elif b%2 == 0: b = round(b/2)
        if c%2 == 1: c = ceil(c/2)
        elif c%2 == 0: c= round(c/2)


# a는 계속 반씩 줄고
# 수가 홀 수 일 때는 ceil
