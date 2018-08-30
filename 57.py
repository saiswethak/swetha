s,k=input().split()
s,k=int(s),int(k)
lst=[int(x) for x in input().split()]
count=0
for i in range(0,s):
    if k==lst[i]:
        count+=1
print(count)
