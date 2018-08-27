n=int(input(" "))
s=1
p=1
count=0
c=0
k=" "
if(n==0):
    print(s)
elif(n<0):
    print("negative number")
else:
    while(count<n):
        if(c==0):
            print(s,end="")
        else:    
             print("",end=k)
             print(s,end="")
        nexterm=s+p    
        s=p
        p=nexterm
        count+=1
        c+=1
