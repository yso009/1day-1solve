n, m = map(int,input().split())
arr = list(map(int,input().split()))

li = []
for i in range(len(arr)-2):   # 5, 6, 7
  for j in range(i+1, len(arr)):
    for k in range(j+1, len(arr)):

      if arr[i]+arr[j]+arr[k] <= m: 
        li.append(arr[i]+arr[j]+arr[k])



print(max(li))