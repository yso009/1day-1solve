score = []
sort_score=[]
for i in range(8):
    a = int(input())
    score.append(a)
    sort_score.append(a)

sort_score.sort(reverse=True)
result_max = 0
result_idx = []
for i in range(5):
    result_max += sort_score[i]
    result_idx.append(score.index(sort_score[i])+1)
result_idx.sort()
print(result_max)
for i in result_idx:
    print(i,end=' ')