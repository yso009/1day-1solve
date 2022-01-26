x,y = map(int,input().split())

def rev(a):
    r = ''
    if a == 0:
        return 0
    else:
        for i in range(len(str(a))-1,-1,-1):
            if str(a)[i] != 0 :
                r += str(a)[i]
        return int(r)
print(rev(rev(x)+rev(y)))
