A,B,C = map(int, input().split())
second = int(input())
second = second+(3600*A)+(60*B)+C
A,B,C = 0,0,0
if second >= 3600:
  A = second // 3600
  second = second-(A*3600)
  if A>=24:
    A = A%24
if 3600> second >= 60:
  B = second // 60
  second = second-(B*60)
  if B>=60:
    B = B%60
if 60> second >=0:
  C = C + second
  second = second-C
  if C>=60:
    C = C%60 

print(A,B,C)