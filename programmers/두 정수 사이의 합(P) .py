def solution(a, b):
    answer = 0
    for i in range(min(a,b),max(a,b)+1):
        answer = answer + i
    return answer

print(solution(3,5))
print(solution(3,3))
print(solution(5,3))