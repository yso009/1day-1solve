a,b = input().split()

result = []

wc = 0
c = 0
while True:

    for i in range(len(a)):
        if a[i] != b[wc+i]:
            c += 1
    result.append(c)
    c = 0
    wc += 1

    if wc + len(a) > len(b):break


print(min(result))


