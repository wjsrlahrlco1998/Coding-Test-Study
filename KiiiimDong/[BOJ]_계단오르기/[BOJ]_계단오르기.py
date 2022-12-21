n = int(input()) # 계단의 개수
a = [int(input()) for i in range(n)] # 계단의 점수를 리스트에 넣음.

t = []
t.append(a[0]) # 맨처음 계단 밟는거(출발점) dp[0] 값
if n > 1: # n이 1 이상일때
    t.append(a[0] + a[1]) # n > 1 보다 클때 이렇게 출력(사실 2일때랑 거의 같은의미) dp[1]값
if n > 2: # n이 2 이상일때
    t.append(max(a[0] + a[2], a[1] + a[2])) # (맨처음칸+ 2칸띄운거), (두칸띄운거+ 그다음칸) 둘 중 하나로 가야한다. dp[2]값 넣어주는거

for i in range(3, n): # dp를 3부터 돌린다.
    t.append(max(t[i-3] + a[i-1] + a[i], t[i-2] + a[i])) # (3칸전꺼(dp저장되어있는거) + 1칸전꺼 + 그칸) (2칸 전꺼(dp저장되어있는것) + 그칸) 둘중 max값

print(t[-1]) # 도착점.