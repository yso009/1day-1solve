def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):        
        x = bin(i)[2:]
        if n > len(bin(i)[2:]):
            x = '0'*(n-len(bin(i)[2:])) + x        
        y = bin(j)[2:]
        if n > len(bin(j)[2:]):
            y = '0'*(n-len(bin(j)[2:])) + y
        q = str(int(x)+int(y))
        if n > len(q):
            q = '0'*(n-len(q))+q
        q = q.replace('0',' ')
        q = q.replace('1','#')
        q = q.replace('2','#')
        answer.append(q)            
    return answer

print(solution(5, [9,20,28,18,11], [30,1,21,17,28]))
print(solution(6,[46,33,33,22,31,50], [27,56,19,14,14,10]))