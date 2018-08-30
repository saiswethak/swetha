sd=input()
count=0
count1=0
for i in range(0,len(sd)):
    if (sd[i]>='a' and sd[i]<='z') or (sd[i]>'A' and sd[i]<'Z'):
        count=1
    elif (sd[i]=='1') or (sd[i]=='2') or (sd[i]=='3') or (sd[i]=='4') or (sd[i]=='5') or (sd[i]=='6') or (sd[i]=='7') or (sd[i]=='8') or (sd[i]=='9') or (sd[i]=='0'):
        count1=1
if count+count1==2:
    print("Yes")
else:print("No")
