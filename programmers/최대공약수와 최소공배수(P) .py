def solution(n, m):
    answer = []
    li_n = []
    li_m = []
    li = []
    li1=[]
    for i in range(1,n+1):
        if n%i == 0:
            li_n.append(i)
    for  i in range(1,m+1):
        if m%i == 0:
            li_m.append(i)
    for i in range(1,max(n,m)+1):
        li.append(n*i)
        li1.append(m*i)

    answer.append(max(set(li_m)&set(li_n)))
    answer.append(min(set(li)&set(li1)))
    print(answer)
    return answer