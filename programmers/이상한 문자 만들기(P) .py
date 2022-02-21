def solution(s):

    li = []
    c = 0
    for i in range(len(s)):
        if s[i].isalpha()==True:
            if c%2==0:
                li.append(s[i].upper())
                c = c+1
            elif c%2==1:
                li.append(s[i].lower())
                c = c+1
        elif s[i].isalpha()==False:
            li.append(s[i])
            c = 0
            
    answer = ''.join(li)
    return answer

print(solution("try hello world"))