def solution(s):
    if 6==len(s) or 4 == len(s):
        answer = s.isdigit()
    else:
        answer = False
    return answer

print(solution("a234"))
print(solution("1234"))