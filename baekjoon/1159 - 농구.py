n = int(input())
li = [input()[0] for _ in range(n)]

dupli_li = set(li)
dupli_li = list(dupli_li)
dupli_li.sort()

result = ''

for i in dupli_li:
    count = li.count(i)
    if count >= 5:
        result += i

if len(result) >=1 :
    print(result)
else:
    print('PREDAJA')
