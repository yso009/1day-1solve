def solution(seoul):
    kim = seoul.index('Kim')
    answer = "김서방은 {}에 있다".format(kim)
    return answer

print(solution(["Jane", "Kim"]))