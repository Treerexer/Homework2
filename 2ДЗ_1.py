def f(num):
    if num == 0:
        return 0
    elif num // 10 == 0:
        return num
    else:
        return (num % 10) + f(num//10)


num = int(input())
print(f(num))
