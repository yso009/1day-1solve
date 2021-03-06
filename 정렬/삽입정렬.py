# 시간 복잡도 = O(n²) 삽입 정렬은 현재 위치에서, 그 이하의 배열들을 비교하여 자신이 들어갈 위치를 찾아, 그 위치에 삽입하는 배열
# 선택한 요소의 앞부분을 보면서 들어갈 자리를 찾아가는 방법
# 삽입정렬은 모두 정렬이 되어 있는 경우에는 단 한번씩만 비교하기 때문에 시간 복잡도가 O(n)이 됨, 그러므로 어느정도 정렬이 된 배열일수록 효율이 높음

li = [8,5,2,6,9,3,1,4,0,7]

for i in range(1, len(li)):
    a = li[i]
    for j in range(i-1, -1, -1):
        if a < li[j]:
            li[j+1] = li[j]
            li[j] = a 
        else:
            break
print(li)
    