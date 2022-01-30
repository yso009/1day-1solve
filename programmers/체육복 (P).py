def solution(n, lost, reserve):   
    ok = [] 
    for i in lost:
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            ok.append(i)
        elif i-1 in reserve:
            reserve.remove(i-1)
            ok.append(i)
        elif i+1 in reserve:
            reserve.remove(i+1)
            ok.append(i)
    answer = n-len(lost)+len(ok)
    return answer

print(solution(5, [2,4], [1,3,5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))