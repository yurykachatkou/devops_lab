
N = int(input())

res = {}

for i in range(N):

    InStr = input().split()
    if InStr[1] == "1":
        res[i] = InStr[0]
if len(res) == 0:
    print(-1)
else:
    print(max(res, key=res.get) + 1)
