def solution(arr):
    answer = []
    if len(arr) == 1:
        answer.append(-1)
    else:
        arr.remove(min(arr))
        for i in range(len(arr)):
            answer.append(arr[i])
    return answer