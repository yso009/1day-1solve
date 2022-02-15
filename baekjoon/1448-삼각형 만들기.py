# n = int(input())
# li = [int(input()) for _ in range(n)]

import sys
n = int(sys.stdin.readline())
li=[]
for i in range(n):
    li.append(int(sys.stdin.readline()))

li.sort(reverse=True)
 
check = True

for i in range(len(li)-2):
    if li[i] < li[i+1] + li[i+2]:
        
        result = li[i] + li[i+1] + li[i+2]
        print(result)     
        check = False
        break

if check == True: print(-1)



