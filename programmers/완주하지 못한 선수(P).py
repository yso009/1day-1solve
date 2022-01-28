import collections
def solution(participant, completion):
    # for i in range(len(completion)):
    #     participant.remove(completion[i])
    # answer = participant[0]
    # return answer
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))