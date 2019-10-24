
N = int(input())
res = []
for i in range(N):
    # Creating list from string by split
    InStr = input().split()
    # Print res if command print
    if "print" in InStr:
        print(res)
    # Form oper string and put it into eval function
    else:
        oper = InStr[0] + "(" + ",".join(InStr[1:]) + ")"
        eval("res." + oper)
