def solution(num):
    c = 0
    while True:
        if num == 1:
            break;
        if num%2 == 0:
            num = num//2
        elif num %2 == 1:
            num = (num*3) +1
        c = c +1
        if num == 1:
            break;
        elif c == 500:
            c = -1
            break
    answer = c
    return answer