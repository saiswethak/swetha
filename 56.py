z=input()
count=0
count1=0
for i in range(0,len(sz)):
    if (z[i]>='a' and z[i]<='z') or (z[i]>'A' and z[i]<'Z'):
        count=1
    elif (z[i]=='1') or (z[i]=='2') or (z[i]=='3') or (z[i]=='4') or (z[i]=='5') or (z[i]=='6') or (z[i]=='7') or (z[i]=='8') or (z[i]=='9') or (z[i]=='0'):
        count1=1
if count+count1==2:
    print("Yes")
else:print("No")
