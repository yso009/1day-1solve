n = int(input())
words = [input() for _ in range(n)]

result = 0
for word in words:
    check = 0
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            check_list = word[i+1:]
            if check_list.count(word[i]) > 0:
                check += 1
    if check == 0:
        result += 1
print(result)