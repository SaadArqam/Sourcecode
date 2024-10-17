def isArmstrong(N):
    num = str(N)
    digits = len(num)
    s = sum(int(digit) ** digits for digit in num)
    return s==N
