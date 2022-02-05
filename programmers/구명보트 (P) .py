from collections import deque
def solution(people, limit):
    people.sort() # 첨에 정렬하구
    people.reverse() #뒤집어버림
    people = deque(people) # deque로 바꿔주고
    c = 0
    for i in range(len(people)):  # 아래 식 보이지?
        # i > limit(100)-40 리미트 - 40 이상이라면 다 count+1
        if people[0] > limit-40:  #여기는 한명만 구해야 하는 무게인 사람들
            c += 1
            people.popleft()
        else:
            break  # 만약 2명을 구해야만 하는 무게면 멈추게함 
    for i in range(len(people)): #ㅇ
        if len(people) == 1:
            c +=1
            break
        elif len(people) == 0:
            break
        elif people[0] + people[-1] <= limit:
            people.pop()
            people.popleft()
            c += 1
        else:
            c += 1
            people.popleft()
    answer = c
    return answer

print(solution([70, 50, 80, 50]	, 100))
print(solution([70, 80, 50], 100))
