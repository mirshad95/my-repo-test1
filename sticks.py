t=int(input())
for h in range(t):
    n=int(input())
    a=[int(i) for i in input().split()]
    a.sort()
    i=0
    b=[]
    while(i<n-1):
        if(a[i]==a[i+1]):
            b.append(a[i])
            i+=2
        else:
            i+=1
    if(len(b)<2):
        print(-1)
    else:
        b.sort()
        print(b[-1]*b[-2])