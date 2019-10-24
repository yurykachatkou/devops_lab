A, B = map(int,input().split())

# if A is negative - find the smallest number.
if "-" in str(A):
    # strip minus
    A = str(A)[1:]
    # sort listA
    listA = sorted(list(A))
    # if the first digit !=0 pop it and save it in variable tmp
    for i, v in enumerate(listA):
        if v != "0":
            tmp = listA.pop(i)
            break
    # add the digit from tmp to sorted listA
    newA = "-" + tmp + "".join(listA)
# if A is positive - find the largest number
else:
    newA = "".join(sorted(list(str(A)),reverse=True))

# if B is negative - find the largest number.
if "-" in str(B):
    # strip minus
    B = str(B)[1:]
    listB = list(B)
    newB = "-" + "".join(sorted(listB,reverse=True))
# if B is positive - find the largest number.
else:
    B = str(B)
    # sort listB
    listB = sorted(list(B))
    # if the first digit !=0 pop it and save it in variable tmp
    for i, v in enumerate(listB):
        if v != "0":
            tmp = listB.pop(i)
            break
    # add the digit from tmp to sorted listB
    newB = tmp + "".join(listB)

res = int(newA) - int(newB)

print(res)

