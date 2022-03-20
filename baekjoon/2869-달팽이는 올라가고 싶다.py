A, B, C = map(int, input().split())  

C = C-B
A = A-B
c,d = divmod(C,A)


if d>0:
  print(c+1)
else:
  print(c)