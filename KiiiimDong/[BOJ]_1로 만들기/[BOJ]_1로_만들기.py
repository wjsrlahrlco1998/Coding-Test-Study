n = int(input())
d = [0] * (n+1) # 테이블 초기화

for i in range(2, n+1) :
    d[i] = d[i-1] + 1 # 1을 빼면 되니깐
    if i % 3 == 0 :
        d[i] = min(d[i], d[i//3]+1)
    if i % 2 == 0 :
        d[i] = min(d[i], d[i//2]+1)

print(d[n])

