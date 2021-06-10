#We can order them as (3, 2, 1). Person 3 is better than Person 2 because his scores in the first two skills are not lesser than Person 2's. 
#And in skill 3, Person 3 scores higher. Similarly, Person 2 is better than Person 1. 
#He scores more than Person 1 in every skill, in fact. 
n = int(input())
def val(e):
    return e[0]


def isBetter(a, b):
    ok = False
    for i in range(3):
        if a[i] > b[i]:
            return False
        if a[i] < b[i]:
            ok = True
    return ok


for _ in range(n):
    s = []
    for _ in range(3):
        s.append(list(map(int, input().split())))
    for i in range(3):
        for j in range(i+1, 3):
            if not isBetter(s[i], s[j]):
                s[i], s[j] = s[j], s[i]

    if isBetter(s[0], s[1]) and isBetter(s[1], s[2]):
        print('yes')
    else:
        print('no'