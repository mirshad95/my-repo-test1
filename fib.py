from collections import Counter
for t in range(int(input())):
    S = input()
    f = [y for x, y in Counter(S).most_common()]
    f = f[::-1]
    if len(f) > 3 and f[3] != f[2] + f[1]:
        f[0], f[1] = f[1], f[0]
    ok = len(f) < 3 or all(f[i] == f[i - 1] + f[i - 2] for i in range(2, len(f)))
    print('Dynamic' if ok else 'Not')