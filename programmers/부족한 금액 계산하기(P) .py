def solution(price, money, count):
    answer = -1
    # 한 바퀴 돌 때 마다 price = price+ (price초깃값)
    # count까지 돌았을때 금액 - money = result
    li = [price*i for i in range(1,count+1)]
    if sum(li) >= money :
        return sum(li)-money
    else:
        return 0

print(solution(3,20,4))