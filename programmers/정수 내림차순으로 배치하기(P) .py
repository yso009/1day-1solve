def solution(n):
    n = str(n)
    li = []
    for i in range(len(n)):
        li.append(n[i])
    li.sort()
    li.reverse()
    print(li)
    answer = int(''.join(li))
    return answer