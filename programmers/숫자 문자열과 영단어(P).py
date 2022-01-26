def solution(s):
        dic = {'one' : '1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9','zero':'0'}
        for i,j in zip(dic.keys(), dic.values()):
            s = s.replace(i,j)
        
        return int(s)


print(solution('2three45sixseven'))