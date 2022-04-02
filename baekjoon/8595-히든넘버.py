n = int(input())
s = input()
e='0'
result = 0
s +='p'
for i in range(len(s)):
  if s[i].isdigit() == True:
    e += s[i]

  else:
    result+=int(e)
    e = '12'

print(result)
