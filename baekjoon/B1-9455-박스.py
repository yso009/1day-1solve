t = int(input())

result = []
for p in range(t): # t번 반복
    n, m = map(int,input().split()) 
    grid= [list(map(int,input().split())) for _ in range(n)] 
    result_x=[] # 거리 값 리스트
    for i in range(m): 
        check = []
        for j in range(n):
            check.append(grid[j][i]) # grid 열을 행으로 변환 후 check에 삽입

        check.reverse()  # 뒤집기
        c = 0
        for k in range(n): 
            if check[k] == 1: # 1을 만나면 c를 result_x에 삽입
                result_x.append(c)
            elif check[k] == 0: # 0일때 c에 1씩 더해서 거리 계산
                c += 1


    result.append(sum(result_x)) 

for answer in result:
    print(answer)
