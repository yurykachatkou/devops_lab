# find the largest number from a combination of digits
def largest(number):
    if number < 0:
        Num = str(number)[1:]
        listNum = sorted(list(Num))
        for i, v in enumerate(listNum):
            if v != "0":
                tmp = listNum.pop(i)
                break
        newNum = "-" + tmp + "".join(listNum)
    elif number == 0:
        newNum = 0
    else:
        newNum = "".join(sorted(list(str(number)), reverse=True))
    return int(newNum)


# find the smallest number from a combination of digits
def smallest(number):
    if number < 0:
        Num = str(number)[1:]
        listNum = list(Num)
        newNum = "-" + "".join(sorted(listNum, reverse=True))
    elif number == 0:
        newNum = 0
    else:
        Num = str(number)
        # sort listB
        listNum = sorted(list(Num))
        # if the first digit !=0 pop it and save it in variable tmp
        for i, v in enumerate(listNum):
            if v != "0":
                tmp = listNum.pop(i)
                break
        # add the digit from tmp to sorted listB
        newNum = tmp + "".join(listNum)
    return int(newNum)


# the biggest difference is when A is the largest number possible,
# and B is the smallest
if __name__ == "__main__":
    A, B = map(int, input().split())
    maxdiff = largest(A) - smallest(B)
