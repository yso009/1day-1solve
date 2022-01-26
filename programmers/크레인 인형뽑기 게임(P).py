def solution(board, moves):
    #  파랑이 1 흰색 2 녹생이3 분홍이 4 갈색 5
    # board의 인덱스를 옮겨줌 1,5,3,5,1,2,1,4 == 4,3,1,1,3,2,4
    result = []
    s = 0
    for i in moves:  # moves만큼
        for j in range(len(board)): 
            if board[j][i-1] != 0:
                result.append(board[j][i-1])
                board[j][i-1] = 0
                break
    #while 문으로 index가 > len(result)-2 break
    #while 문 내에서 없앨 때 마다 index를 0으로 초기회
    index = 0
    while len(result) > 1:
        if result[index] == result[index+1]:
            del result[index]
            del result[index]
            index = 0
            s+=2
        else:
            index += 1
        if index == len(result)-1:
            break
    answer = s
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4] ))