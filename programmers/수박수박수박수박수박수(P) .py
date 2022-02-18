def solution(n):
    if n%2 == 0:
        wm = "수박"*(n//2)
    elif n%2 != 0 :
        wm = "수박"*(n//2)+"수"
    answer = wm
    return answer

print(solution(3))
print(solution(4))