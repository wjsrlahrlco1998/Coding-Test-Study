from collections import deque

def solution(queue1, queue2):
    # 0. 횟수를 담을 변수 정의
    answer = 0

    # 1. 리스트를 큐 구조로 전환
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    # 2. 리스트의 합을 미리 계산
    target_sum = (sum(queue1) + sum(queue2)) // 2
    queue1_sum = sum(queue1)

    # 3. 큐 원소 작업
    while queue1 and queue2: # 큐의 원소가 없는 경우 정지
        # 1) queue1의 합이 목표 합보다 작은 경우
        if queue1_sum < target_sum: 
            pop_value = queue2.popleft()
            queue1_sum += pop_value
            queue1.append(pop_value)
            answer += 1
        # 2) queue1의 합이 목표 합보다 큰 경우
        elif queue1_sum > target_sum:
            pop_value = queue1.popleft()
            queue1_sum -= pop_value
            answer += 1
        # 3) queue1의 합이 목표 합과 같은 경우
        else:
            return answer
    
    # 4. 두 큐의 합이 같아질 수 없는 경우
    else:
        return -1 