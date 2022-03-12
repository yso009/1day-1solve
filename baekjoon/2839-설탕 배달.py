x = int(input())
order=x
five=0
three=0
while order>0:
	if order%5==0:
		five+=order//5
		break
	order-=3
	three+=1

if (five*5)+(three*3)==x:
	print(five+three)
else:
	print(-1)
