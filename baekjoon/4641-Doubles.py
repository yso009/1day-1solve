while True:
  c = 0
  arr = list(map(int,input().split()))
  if arr.count(-1):
    break
  else:
    for i in range(len(arr)-1):
      if arr[i]*2 in arr:
        c += 1
  print(c)