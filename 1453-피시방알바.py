n = int(input())
sit_number = input().split()
c = 0
for i in range(len(sit_number)-1):
    for j in range(i+1, len(sit_number)):
        if sit_number[i] == sit_number[j]:
            c += 1
            break
print(c)