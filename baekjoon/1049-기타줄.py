n, m = map(int,input().split())

a = [list(map(int,input().split())) for _ in range(m)]

min_6 = a[0][0]
min_1 = a[0][1]

result = 0

for i in range(1, len(a)):
    if min_6 > a[i][0]:
        min_6 = a[i][0]
    if min_1 > a[i][1]:
        min_1 = a[i][1]


if min_6 >= (min_1 * 6):
    result = (n * min_1)

else: # 묶음이 더 쌀때
    while True:
        if n > 6:
            n = n - 6
            result += min_6
        else:
            if n * min_1 > min_6:
                result += min_6
                break
            else:
                result += n*min_1
                break
print(result)
            


