def solution(strings, n):
    answer = []
    answer1=[]
    for i in strings:
        answer1.append(i[n]+i)
    answer1.sort()
    for i in answer1:
        answer.append(i[1:])
    return answer

print(solution(['sun','bad', 'car'], 1))
print(solution(["abce", "abcd", "cdx"],	2))