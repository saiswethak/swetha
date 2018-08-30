nm,s=input().split()
nm,s=int(nm),int(s)
lst=[int(x) for x in input().split()]
count=0
for i in range(0,nm):
    if s==lst[i]:
        print("yes")
        break
else:print("no")
