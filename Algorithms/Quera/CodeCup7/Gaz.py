from decimal import *
import math

t = int(input())
nums = []
for i in range(t):
    num = input().split()
    nums.append(num)


def circle(fnum, snum):
    if fnum == snum:
        if (2 * fnum * (math.pi) / 4) < 2 * fnum:
            return fnum * (math.pi) / 2
        else:
            return fnum * 2
    else:
        if fnum < snum:
            return min((fnum * (math.pi) / 2 + snum - fnum), (fnum + snum))
        else:
            return min(((snum * (math.pi) / 2) + fnum - snum), (fnum + snum))


def cal(num):
    if num[0] == 0:
        if num[2] == 0:
            return abs(num[3] - num[1])
        else:
            if num[1] == 0:
                return float(abs(num[2]))
            else:
                return circle(abs(num[1]), abs(num[2]))
    else:
        if num[2] == 0:
            if num[3] == 0:
                return abs(float(num[0]))
            else:
                return circle(abs(num[0]), abs(num[3]))
        else:
            return float((num[2]) - (num[0]))


for num in nums:
    getcontext().prec = 30
    num1 = [float(item) for item in num]
    x = cal(num1)
    x = (x) / 1000
    print("%f" % abs(Decimal(x) * Decimal(1000)))
