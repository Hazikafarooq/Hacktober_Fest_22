def mult(a, b):
     if a == 0 or b == 0:
         return 0
     else:
         return b + mult(a-1, b)

a = int(input())
b = int(input())

print(mult(a, b))
