def solution(d, budget):
    d.sort()
    answer = 0
    while True:
        if budget <= 0 or len(d)==0 or budget - d[0] < 0 :
            break
        elif budget - d[0] >=0:
            budget = budget - d[0]
            del d[0]
            answer = answer + 1
    return answer

print(solution([1,3,2,5,4],9))
print(solution([2,2,3,3], 10))