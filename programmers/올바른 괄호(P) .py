def solution(s):
    answer = True 
    x = 0  
    if s[0] == ')' or s[len(s)-1] == '(':
        return False
    for i in range(len(s)):
        if s[i] == '(':
            x += 1
        elif s[i] == ')':
            x -= 1
        if x < 0:
            answer = False
    if x != 0:
        answer = False
    return answer


print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))