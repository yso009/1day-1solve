def solution(nums):
    answer = list(set(nums))
    if len(nums)//2 > len(answer):
        return len(answer)
    elif len(nums)//2 == len(answer):
        return len(nums)//2
    elif len(nums)//2 < len(answer):
        return len(nums)//2

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))