# 1. 입력받기
m = int(input()) # m이상
n = int(input()) # n이하

# 2. 소수 걸러내는 함수
def is_prime_number(x): # 소수일 때 True인 함수
    if x == 1: # 1일때는 걸러준다.(2부터 적용되는 알고리즘이라서)
        return False 
    else:
        for i in range(2, x): # 2부터
            if x % i == 0: # 나눠지는 원소가 있으면 False(소수가 아니니깐)
                return False
        return True # 나눠지지 않으면 소수니깐 True

# 3. 카운트
cnt_list = [] # 카운트하기위한 리스트
for i in range(m, n+1): # m 이상 n 이하
    if is_prime_number(i) == True: # 소수일때 
        cnt_list.append(i) # 리스트에 넣는다.

# 4. 출력
if len(cnt_list) == 0: # 리스트가 비어있으면 소수가 없다는 뜻이므로 -1출력
    print(-1)
else: # 리스트가 비어있지 않을 때
    print(sum(cnt_list)) # 합계 출력
    print(min(cnt_list)) # 최소값 출력

