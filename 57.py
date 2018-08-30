s,z=input().split()
s,z=int(s),int(z)
lst=[int(x) for x in input().split()]
count=0
for i in range(0,s):
    if z==lst[i]:
        count+=1
print(count)
