N, K = map(int,input().split())
coin = list()

for i in range (N):
    coin.append(int(input()))

count=0
for i in reversed(range(N)): # 가장 큰 동전으로 나눌 수 있게 뒤집음
    count += K // coin[i] # K를 동전으로 나눈 정수몫을 count에 더함
    K = K % coin[i] # K를 동전으로 나눈 나머지를 K에 저장

print(count)

# 예를 들어 1800원과 500원 400원 100원이 있다고 했을 떄, 
# 1800//500=3(정수몫) 500원을 3개 쓴 것. count에 더하여 저장
# 1800 % 500 =300(나머지)
# 300//400=0(정수몫) 400원을 0개 쓴 것. count에 더하여 저장
# 300 % 400 =300(나머지)
# 300//300=1정수몫) 300원을 1개 쓴 것. count에 더하여 저장
# 300 % 300 =0(나머지)
# count에 저장된 0+3+0+1=4