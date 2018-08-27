s=int(input(""))
lst=[int(x) for x in input().split()]
v1=0
for i in range(0,s):
    v1+=lst[i]
print(int(v1/s))
