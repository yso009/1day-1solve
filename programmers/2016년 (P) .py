def solution(a, b):
    day = ["THU","FRI","SAT","SUN","MON","TUE","WED"]  #1월 1일 금
    month = [31, 29, 31, 30, 31, 30 , 31, 31, 30, 31, 30, 31]
    # a-1 a가 5월달이면 4번째 인덱스를 가져와야함.

    
    return day[(sum(month[:a-1]) + b) % 7]

print(solution(5,24))