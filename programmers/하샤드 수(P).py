def solution(x):
#     x = str(x)
#     li = []
#     for i in range(len(x)):
#         li.append(int(x[i]))

#     if int(x)%sum(li) == 0:
#         answer = True
#     else:
#         answer = False
#     return answer

    return x % sum([int(i) for i in str(x)]) == 0