n = int(input()) # 케이크 길이
m = int(input()) # 방청객 수

li = [list(map(int,input().split())) for _ in range(m)] # 2차원 배열로 원하는 길이 입력
max_n = [] # 예상되는 큰 수 

result = []

cake = [True for _ in range(n+1)]
cake[0] = False

for i in range(len(li)):
    c = 0
    for j in range(li[i][0], li[i][1]+1):
        if cake[j] == True:
            cake[j] = str(i+1)  # 방청객 1도 True로 인식해서 Str형식으로 변환
            c +=1 
    result.append((c, i+1))  # 받는 조각 수 , 방청객 번호로 저장

result.sort(key=lambda x:(-x[0], x[1]))

for i in range(len(li)):
    max_n.append(li[i][1]- li[i][0])

print(max_n.index(max(max_n))+1) # 가장 많은 조각을 받도록 예상되는 방척객의 번호
print(result[0][1])



