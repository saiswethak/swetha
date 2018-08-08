n,m=input().split()
n,m=int(n),int(m)
count=0
for i in range(n+1,m):
    if(i%2!=0):
        if i<m-2:
            k=" "
        else:k=""
        print(i,end=k)
