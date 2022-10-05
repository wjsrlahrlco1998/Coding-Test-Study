doc = input()
word = input()

cnt = 0

while doc.find(word) != -1:
    doc = doc.replace(word, " ", 1)
    cnt += 1

print(cnt)