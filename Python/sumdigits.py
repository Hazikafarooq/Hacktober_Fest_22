def sum_digits(n):
    s = 0 
    while n > 0:
        a = n%10
        n = n//10
        s = s + a
    return s

print(sum_digits(65))
