#There is one cat and one dog. The number of legs of these animals on the ground are 8, it can be possible when both cat and dog are standing on the ground.

t=int(input())
for i in range(t):
    c,d,l=input().split()
    c,d,l=int(c),int(d),int(l)
    maxi=4*(c+d)
    if(d*2<c):
        mini=4*(c-d)
    else:
        mini=4*d
    if(l%4==0 and l>=mini and l<=maxi):
        print('yes')
    else:
        print('no')