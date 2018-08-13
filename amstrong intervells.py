s,p=map(int,input().split())
count=0
for i in range(s,p):
    le=len(str(i))
    sum1=0
    temp=i
    while i>0:
        x=i%10
        sum1=sum1+(x**le)
        i=i//10
    if(sum1==temp):
        if(count==0):
            print(temp,end="")
        else:
            print("",end=" ")
            print(temp,end="")
        count=count+1
