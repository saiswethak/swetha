sp,k=input().split()
sp,k=int(sp),int(k)
lst=[int(x) for x in input().split()]
count=0
for i in range(0,sp):
    if k==lst[i]:
        count+=1
print(count)
