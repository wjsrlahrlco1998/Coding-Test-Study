n = int(input())

for _ in range(n):
    cnt = []
    s = input()
    for p in s:
        if p == '(':
            cnt.append(p)
        elif p == ')':
            cnt.append(p)
            if len(cnt) > 1:
                cnt.pop()
                cnt.pop()
            else:
                break

    if len(cnt) != 0:
        print("NO")
    else:
        print("YES")

