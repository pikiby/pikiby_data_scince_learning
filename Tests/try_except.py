def division(a, b):
    try:
        c = a / b
    except ZeroDivisionError:
        print("Zero division error!")
        return
    return c

print(division(1, 0))
print(division(1, 1))


