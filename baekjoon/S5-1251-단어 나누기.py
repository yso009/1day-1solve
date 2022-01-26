word = list(input())


g = []
for i in range(1,len(word)-1):  # 1~
    for j in range(i+1,len(word)):
        word1 = word[:i]
        word2 = word[i:j]
        word3 = word[j:]
        
        word1.reverse()
        word2.reverse()
        word3.reverse()
        g.append(word1 + word2 + word3)

g.sort()
r = ''
print(r.join(g[0]))

