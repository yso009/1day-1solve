def solution(n): #int형
    n = str(n)

    return list(reversed([int(n[i]) for i in range(len(n))]))