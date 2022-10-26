channel = int(input())
n = int(input())
if n == 0:
    x_buttons = set()
else:
    x_buttons = set(map(int, input().split()))

count = abs(channel - 100) # +,-로만 채널이동하는 경우

for nums in range(1000001):
    nums = str(nums)

    for i in range(len(nums)): #각 자리 숫자 확인
        if int(nums[i]) in x_buttons:
            break
    else:
        count = min(count, len(nums) + abs(int(nums)-channel)) #숫자 누른 횟수와 +,- 버튼 누르는 횟수

print(count)