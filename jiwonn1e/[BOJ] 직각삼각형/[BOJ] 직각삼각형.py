while True:
    l = list(map(int,input().split()))
    if sum(l) == 0:
        break
    else:
        l.sort()
        if l[0]**2 + l[1]**2 == l[2] **2:
            print("right")
        else:
            print("wrong")