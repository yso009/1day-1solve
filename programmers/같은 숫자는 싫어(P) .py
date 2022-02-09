def solution(arr):
    answer = []
    arr.append("g")
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            answer.append(arr[i])
    return answer


print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))