import time
#50회 미만으로
d = [0] * 50

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)#함수안에서 함수를 사용해서 러닝타임축소
    print(d)
    return d[x]

res = fibo(10)
print(res)


"""
for num in range(5, 40, 10):
    start = time.time()
    print(num)
    res = fibo(num)
    print(res, '-> 러닝타임:', round(time.time() - start, 2), '초')
"""