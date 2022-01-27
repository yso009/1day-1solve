def solution(a, b):
    # c = 0
    # for i in range(len(a)):
    #     c = c + a[i] * b[i]
    # sum[i*j for i,j in zip(a,b)]
        
    return sum([ i*j for i,j in zip(a,b)])



print(solution([1,2,3,4],[-3,-1,0,2]))
print(solution([-1,0,1],[1,0,-1]))