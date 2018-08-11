s,p=map(int,raw_input().split())
for i in range(s,p):
    l=len(str(i))
    sum=0
    temp=i
    while i>0:
        x=i%10
        sum=sum+(x**1)
        i=i/10
    if(sum==temp):
        print(temp)
