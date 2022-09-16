N, M = map(int, input().split())
board = []
count = []
for _ in range(N):
    board.append(input())

for i in range(N-7):
    for j in range(M-7):
        cnt1, cnt2 = 0, 0
        for k in range(i, i + 8):
            for l in range(j, j+8):
                if (k + l) % 2 ==0:
                    if board[k][l] != 'W':
                        cnt1 += 1
                    if board[k][l] != 'B':
                        cnt2 += 1
                else:
                    if board[k][l] != 'B':
                        cnt1 += 1
                    if board[k][l] != 'W':
                        cnt2 += 1
        count.append(cnt1)
        count.append(cnt2)

print(min(count))