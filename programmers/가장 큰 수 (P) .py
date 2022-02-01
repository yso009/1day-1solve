from itertools import permutations

def solution(numbers):
    li=[]
    for i in range(len(numbers)):
        li.append([str(numbers[i])*4,i]) # 한 자리 숫자를 3자리로 바꿔줌
    li.sort(reverse=True)
    
    r=''
    for i in range(len(li)):
        r+=str(numbers[li[i][1]])
    r = int(r)
    r = str(r)
    return r
    
    
#     result =[]
#     s =''.join(map(str,numbers))
#     r =''
#     li = list(permutations(numbers, len(numbers)))
#     for i in range(len(li)):
#         r += ''.join(map(str,li[i]))
#         if len(r) == len(s):
#             result.append(int(r))
#             r = ''
#     print(result)
#     answer = max(result)
#     return str(answer)


print(solution([6,10,2]))
print(solution([3,30,34,5,9]))