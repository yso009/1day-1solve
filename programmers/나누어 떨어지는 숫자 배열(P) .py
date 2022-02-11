from tkinter import SOLID


def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    answer.sort()
    if len(answer) == 0:
        answer.append(-1)

    return answer

print(solution([5,9,7,10], 5))
print(solution([2,37,1,3], 1))
print(solution([3,2,6], 10))