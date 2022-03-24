N = int(input())
li = [input() for _ in range(N)]
for i in li:
  print(i[0].upper()+i[1:])
