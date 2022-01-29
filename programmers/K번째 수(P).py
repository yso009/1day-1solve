def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):  # commands[0][1][2]
        li = []
        for j in range(len(commands[i])): # 2 5 3 / 4 4 1 / 1 7 3
            li.append(commands[i][j])
        x = array[li[0]-1:li[1]]
        x.sort()
        answer.append(x[li[2]-1])
        # return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))