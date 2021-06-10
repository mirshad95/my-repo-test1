def mnmx(n,l):
    x=min(l)
    print((n-1)*x)

t=int(input())

for i in range(t):
    n=int(input())
    l=[int(x) for x in input().split()]
    mnmx(n,l)