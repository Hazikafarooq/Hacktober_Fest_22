def exp(a, b):
    if a == 0:
        return 0
    elif b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * exp(a, b-1)

a = int(input())
b = int(input())
print(exp(a, b))
