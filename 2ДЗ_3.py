def f(num, x):
    if x == 0:
        return 0
    elif x == 1:
        return num
    else:
        return num * f(num, x-1)


num = int(input())
power = int(input())
print(f(num, power))
