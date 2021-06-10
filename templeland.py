#In the first strip, all the conditions are satisfied, hence it is valid.

#In the second strip, it does not start with a 1, and hence is invalid.

#In the third strip, it keeps increasing even past the centre, instead of decreasing. Hence invalid.

#The fourth strip does not increase and decrease by exactly 1. Hence invalid.

#The fifth satisfies all conditions and hence is valid.

#The sixth and seventh strip do not have a 'centre' part. Because for every part, there are either more parts to its right than its left, or more parts on its left than its right. Hence both the strips are invalid.

for x in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    count=0
    a=[]
    for i in range(1,n//2+1):
        a.append(i)
    for i in range(n//2+1,0,-1):
        a.append(i)
    if a==s:
        print('yes')
    else:
        print('no')