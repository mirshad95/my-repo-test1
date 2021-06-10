for _ in range(int(input())):
    a,b,n=map(int,input().split())
    if(n%2!=0):
        a=a*2
    print(max(a,b)//min(a,b))    
