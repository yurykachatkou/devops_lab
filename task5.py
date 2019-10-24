InStr = str(input())
x = {}

for k in InStr:
    if k not in x:
        x[k] = 1
    else:
        x[k] += 1

srt = sorted(x.items(), key=lambda z: (-z[1], z[0]))[0:3]

for i in srt:
    print(i[0], i[1])
