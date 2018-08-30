m=input()
count=0
for i in range(0,len(m)):
    if m[i]=='0' or m[i]=='1':
        count+=1
if count==len(m):
    print("yes")
else:print("no")
