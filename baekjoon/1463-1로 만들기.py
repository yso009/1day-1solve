n = int(input())

c = 0
while True:
    if n % 3 == 0:
        n = n//3
        c += 1
    elif n % 2 == 0:
        n = n//2
        c += 1
    elif n%3 !=0 and n%2 !=0:
        n = n-1
        c += 1
    if n == 1:
        break 
print(c)