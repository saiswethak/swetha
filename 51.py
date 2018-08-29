p=int(input())
a=[]
rev=0

count=0
while p>0:
    temp=p%10
    rev=rev*10+temp
    p=p//10
    count+=1
while rev>0:
    temp=rev%10
    a.append(temp)
    rev=rev//10
for i in range(0,count):
    if i<count-1:
        k=' '
    else:k=''
    print(a[i],end=k)
