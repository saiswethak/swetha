t=input()
c=0
for i in t:
    if(i>='A' and i<='Z' or i>='a' and i<='z' or i.isdigit()):
       a=3
    else:
       c+=1
print(c)
