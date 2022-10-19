# 1. 기본세팅
import math # 제곱근 활용하기 위해서
import sys # input 바꿔주기 위해서
input = sys.stdin.readline # input 시간복잡도 낮춰줌.

# 2. for문에서 거리에 따른 규칙 적용
n = int(input()) # 테스트케이스의 수
for i in range(n): # 테스트케이스 개수 만큼 반복
    x, y = map(int, input().split()) # x, y 지점 입력
    distance = y - x # 총 거리(x에서y까지)
    root = math.floor(math.sqrt(distance)) # floor: 버림
    
    if distance == math.pow(root, 2): # (거리가 루트씌워서 버림 한거의 제곱이랑 같으면) == (제곱수라는 뜻) 
        print(2 * root - 1) # 제곱근해서 버린거*2 -1
    elif distance <= math.pow(root, 2) + root: # (거리가 루트씌워서 버림 한거의 제곱 + 루트씨워서 버림한거 보다 작거나 같을 때는)
        print(2 * root) # 제곱근해서 버린거*2
    else: # (거리가 루트씌워서 버림 한거의 제곱 + 루트씨워서 버림한거 보다 클 때는)
        print(2 * root + 1) # 제곱근해서 버린거*2 +1