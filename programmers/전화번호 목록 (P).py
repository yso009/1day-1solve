def solution(pb):
    pb.sort()
    x = 0
    for i in range(1,len(pb)):
        if pb[0] == pb[i][0:len(pb[0])]:
            x = x +1     
        else:
            x = x
    if x == 0:
        answer = True
        return answer
    if x > 0 :
        answer = False
        return answer

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))