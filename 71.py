m=input()
ch=[]
for i in range(0,len(m)):
    ch.append(m[i])
k=[]
i=len(m)-1
count=0
while i>=0:
    k.append(m[i])
    i-=1
for i in range(0,len(ch)):
    if ch[i]==k[i]:
        count+=1
if count==len(ch):
    print("yes")
else:print("no")
