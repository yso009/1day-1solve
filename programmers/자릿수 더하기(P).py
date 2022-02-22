def solution(n):
    s = 0
    n = str(n)
    for i in range(len(n)):
        s = s + int(n[i])
    answer = s
    return answer
