queue1 = [1, 1]
queue2 = [1, 5]

# 리스트 타입의 pop을 진행하기 위한 함수
def queue_pop(queue):
    queue_reverse = queue[::-1]
    pop_value = queue_reverse.pop()
    queue = queue_reverse[::-1]
    return pop_value, queue

def solution(queue1, queue2):
    # 0. 횟수를 담을 변수 정의
    answer = 0

    # 1. 큐 원소 작업
    while True:
        # * 두 큐의 합이 같은 경우가 없는 경우 : 최대 교환 개수를 넘어가는 경우
        if len(queue1) * len(queue2) < answer :
            return -1

        if sum(queue1) == sum(queue2):
            print(sum(queue1), sum(queue2))
            return answer
        else:
            # 1) queue1의 합이 queue2의 합보다 큰 경우
            if sum(queue1) > sum(queue2):
                queue1_pop, queue1 = queue_pop(queue1)
                queue2.append(queue1_pop)
                answer += 1
            # 2) queue2의 합이 queue1의 합보다 큰 경우
            elif sum(queue1) < sum(queue2):
                queue2_pop, queue2 = queue_pop(queue2)
                queue1.append(queue2_pop)
                answer += 1

print(solution(queue1, queue2))