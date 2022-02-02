def solution(numbers):
    # answer = set()
    # for i in range(len(numbers)):  #0,1,2,3,4
    #     for j in range(i+1, len(numbers)):  # i = 0 / 1,2,3,4 / i=1 / 2,3,4
    #         answer.add(numbers[i] + numbers[j])
    # answer = list(answer)
    # return sorted(answer)
    answer = list()
    for i in range(len(numbers)):  #0,1,2,3,4
        for j in range(i+1, len(numbers)):  # i = 0 / 1,2,3,4 / i=1 / 2,3,4
            if numbers[i] + numbers[j] not in answer:
                answer.append(numbers[i]+numbers[j])
    answer.sort()
    return answer

print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))

