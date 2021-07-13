N = int(input())
X = list(map(int,input().split()))
X.sort()

Group = 0

while X != None:
    if X != None:
        if len(X) != 1:
            del X[-1], X[0]
            Group += 1
        else:
            break
print(Group)