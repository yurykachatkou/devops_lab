InStr = input()
x = {}

for k in InStr:
    x[k] = x.get(k, 0) + 1

srt = sorted(x.items(), key=lambda z: (-z[1], z[0]))[0:3]

for i in srt:
    print(i[0], i[1])
