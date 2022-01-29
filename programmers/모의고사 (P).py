def solution(answers):
    answer = []
    result = []
    no1 = 1,2,3,4,5
    no2 = 2,1,2,3,2,4,2,5
    no3 = 3,3,1,1,2,2,4,4,5,5
    count1 = 0
    count2 = 0
    count3 = 0
    for i in range(0,len(answers)):
        if answers[i] == no1[i%len(no1)]:
            count1 = count1+1
        if answers[i] == no2[i%len(no2)]:
            count2 = count2+1
        if answers[i] == no3[i%len(no3)]:
            count3 = count3+1
    if count1 == count2 == count3:
        answer.append(1)
        answer.append(2)
        answer.append(3)
    elif count1 == count2 > count3:
        answer.append(1)
        answer.append(2)
    elif count1 == count3 > count2:
        answer.append(1)
        answer.append(3)        
    elif count2 == count3 > count1:
        answer.append(2)
        answer.append(3)
    elif max(count1,count2,count3)==count1:
        answer.append(1)
    elif max(count1,count2,count3)==count2:
        answer.append(2)        
    elif max(count1,count2,count3)==count3:
        answer.append(3)
        print(answer)
    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))