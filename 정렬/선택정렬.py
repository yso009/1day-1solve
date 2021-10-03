# 시간 복잡도 = O(n²) 현재 위치에 들어갈 값을 찾아 정렬하는 배열,

li = [8,5,2,6,9,3,1,4,0,7]

for i in range(len(li)-1):    
    for j in range(i+1, len(li)):
        if li[i] > li[j]:
            li[i], li[j] = li[j], li[i]
print(li)
