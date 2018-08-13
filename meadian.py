def median(s,n):
    s.sort()
    if n%2==0:
        return s[n/2]
    else:
        return (s[n/2-1]+s[n/2])/2
n=int(raw_input())
s=[int(x) for x in raw_input().split()]
print (median(s,n-1))
