n= int(input())

# 몫이 n보다 커질 수 없다.
# if a > n :
#   break

c = 0
q = n+1

for i in range(q,(n**2)+1,q):
    c += i
# for i in range(n,(n**2)+1):

print(c)



# 몫과 나머지가 같은 첫번째 수를 찾는다 > 몫이 1 나머지가 1인 수 즉, n +1 인 수
# 그 수의 배수를 범위 안에 몇개가 있는지 찾는다.

