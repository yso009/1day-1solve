def solution(numbers, hand):
    x, y = 0, 1
    position = {1:(0,0), 2:(0,1), 3:(0,2), \
                4:(1,0), 5:(1,1), 6:(1,2), \
                7:(2,0), 8:(2,1), 9:(2,2), \
                '*':(3,0) , 0:(3,1), '#':(3,2)}
    lh = position["*"] #좌표값
    rh = position["#"] #좌표값   
    for i in range(len(numbers)):
        if numbers[i] in [1, 4, 7]:
            lh = position[numbers[i]]
            numbers[i] = "L"
            
        elif numbers[i] in [3,6,9]:
            rh = position[numbers[i]]
            numbers[i] = "R"
        elif numbers[i] in position:
            if abs(position[numbers[i]][x] - rh[x]) + abs(position[numbers[i]][y] - rh[y]) > \
            abs(position[numbers[i]][x] - lh[x]) + abs(position[numbers[i]][y] - lh[y]):
                lh = position[numbers[i]]
                numbers[i] = "L"
            elif abs(position[numbers[i]][x] - rh[x]) + abs(position[numbers[i]][y] - rh[y]) < \
            abs(position[numbers[i]][x] - lh[x]) + abs(position[numbers[i]][y] - lh[y]):
                rh = position[numbers[i]]
                numbers[i] = "R"
            elif abs(position[numbers[i]][x] - rh[x]) + abs(position[numbers[i]][y] - rh[y]) == \
            abs(position[numbers[i]][x] - lh[x]) + abs(position[numbers[i]][y] - lh[y]):
                if hand =="right":
                    rh = position[numbers[i]]
                    numbers[i] = "R"
                else:
                    lh = position[numbers[i]]
                    numbers[i] = "L"
    answer = ''.join(numbers)
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))