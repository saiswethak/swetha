n=int(input(" "))
s=1
p=1
count=0
if(n==0):
    print(a)
elif(n<0):
    print("postive number")
else:
    while(count<n):
        print(s,sep=' ',end=' ')
        nexterm= s+p
        s=p
        p=nexterm
        count+=1
