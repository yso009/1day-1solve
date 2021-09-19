a = int(input())
n = 64
c = 0
if n%a == 0:
    print(1)
else:
    while True:
        if a == 0:
            break
        if n > a:
            n = n/2
        else:
            a = a%n
            c = c+1        
    print(c)        
