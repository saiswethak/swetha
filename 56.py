sp=input()
count=0
count1=0
for i in range(0,len(sp)):
    if (sp[i]>='a' and sp[i]<='z') or (sp[i]>'A' and sp[i]<'Z'):
        count=1
    elif (sp[i]=='1') or (sp[i]=='2') or (sp[i]=='3') or (sp[i]=='4') or (sp[i]=='5') or (sp[i]=='6') or (sp[i]=='7') or (sp[i]=='8') or (sp[i]=='9') or (sp[i]=='0'):
        count1=1
if count+count1==2:
    print("Yes")
else:print("No")
