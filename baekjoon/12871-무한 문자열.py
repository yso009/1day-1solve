s = input()
t = input()

#최대공약수

a, b = len(s), len(t)
def dirtn(s,t):
    global a,b
    if a == 0 : 
        return b
    elif b == 0:
        return a
    if a >= b:
        a = a % b
    elif a <= b:
        b = b % a
    return dirtn(a,b)

def main(s,t): 
    x = (a*b)//dirtn(a,b)
    if s == t: return 0
    else: 
        s = s*(x//len(s))
        t = t*(x//len(t))
        if s == t:
            return 1
        else: return 0
print(main(s,t))
