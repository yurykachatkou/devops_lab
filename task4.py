
N = int(input())

res = {}

for i in range(N):

    InStr = input().split()
    if InStr[1] == "1":
        res[i] = InStr[0]

if not res:
    print(-1)
else:
    print(max(res, key=res.get) + 1)
