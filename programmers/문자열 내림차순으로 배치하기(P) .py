def solution(s):
    li = []
    up = []
    low = []
    for i in range(len(s)):
        li.append(s[i])
    for i in li:
        if i.isupper() == True:
            up.append(i)
        else:
            low.append(i)
    low.sort()
    low.reverse()
    up.sort()
    up.reverse()
    low.extend(up)
    return ''.join(low)

print(solution("Zbcdefg"))