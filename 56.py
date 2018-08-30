m=input()
count=0
count1=0
for i in range(0,len(m)):
    if (m[i]>='a' and m[i]<='z') or (m[i]>'A' and m[i]<'Z'):
        count=1
    elif (m[i]=='1') or (m[i]=='2') or (m[i]=='3') or (m[i]=='4') or (m[i]=='5') or (m[i]=='6') or (m[i]=='7') or (m[i]=='8') or (m[i]=='9') or (m[i]=='0'):
        count1=1
if count+count1==2:
    print("Yes")
else:print("No")
