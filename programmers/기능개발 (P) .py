from collections import deque

def solution(progresses, speeds):
    result =[]
    progresses = deque(progresses)
    speeds = deque(speeds)
    progresses.append(-1)
    c = 0
    while True:
        c = 0
        if len(progresses) == 1:
            break
        if progresses[0] >= 100:
            for i in progresses:
                if i >=100:
                    c += 1
                else:
                    result.append(c)
                    break
            for i in range(c):
                progresses.popleft()
                speeds.popleft()
        else:
            for i in range(len(progresses)-1):
                progresses[i] += speeds[i]
    return result


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))
