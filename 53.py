m=int(input())
count=0
sum=0
while m>0:
    rem=m%10
    sum=sum+rem
    m=m//10
print(sum)
