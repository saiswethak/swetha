num,num1,num2=raw_input().split
num,num1,num2=int(num) , int(num1) , int(num2)
if(num>num1) and (num>num2):
	print(num)
elif(num1>num2):
	print(num1)
else:
	print(num2)
