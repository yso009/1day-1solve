import math
def solution(n, words):
    answer = [0,0]
    li = []
    # 첫 번째 조건 words의 끝 글자와 다음 words의 첫 글자 비교
    # 두 번째 조건 첫 번째 조건 충족 후 words가 2개 인지 확인
    # 세 번째 조건 탈락자가 없다면 0,0 출력
    
    for i in range(1, len(words)):  
        if words[i-1][-1] == words[i][0]: # 앞에 인덱스의 끝 글자와 현재 인덱스의 첫 글자가 같다면,
            for j in range(i): # 처음부터 i까지 돌린다.
                if words[j] == words[i]:  # 범위를 i보다 앞쪽으로                                        
                    li.append((i%n)+1)
                    li.append(math.ceil((i+1)/n))
                    break
        else:
            li.append((i%n)+1)  
            li.append(math.ceil((i+1)/n))
            break

    if len(li) == 0:
        return answer
    else:
        answer[0] = li[0]
        answer[1] = li[1]
    return answer

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5,["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2,["hello", "one", "even", "never", "now", "world", "draw"]))