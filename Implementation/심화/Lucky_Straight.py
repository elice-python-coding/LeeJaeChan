score = (input())
length = len(score)
summary = 0

for l in range(length // 2):
    summary += int(score[l])

for r in range(length // 2, length):
    summary -= int(score[r])

if summary == 0:
    print("LUCKY")

else:
    print("READY")
