def f(lst):
    if not lst:
        return 0
    elif len(lst) == 1:
        return lst
    else:
        return lst[-1]+f(lst[:-1])


lst = input()
lst2 = (f(lst))
if lst == lst2:
    print("Палиндром")
else:
    print("Не палиндром")
