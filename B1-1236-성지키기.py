#. . . . . . . .   
#. . . . . . . .
#X . . . . . . .
#. . . . . . . .
#. . . . . . . .
#가로줄에서 필요한 X 4개
#세로줄에서 필요한 X 7개

r,c = map(int,input().split())
castle = [input() for _ in range(r)]

castle_col =[]
row_x, col_x = 0, 0

 
for i in castle:  # 가로줄에 X가 없으면 row_x 에 1을 추가
    if 'X' not in i:
        row_x += 1

for i in range(c): # 세로줄로 정렬해서 castle_col에 추가
    s= ''
    for j in range(r):
        s += castle[j][i]
    castle_col.append(s)


for i in castle_col: #세로줄로 정렬한 것에 X가 없으면 col_x 에 1을 추가 
    if 'X' not in i:
        col_x += 1
    
print(max(row_x, col_x ))