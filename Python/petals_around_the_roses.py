d1 = int(input())
d2 = int(input())
d3 = int(input())
d4 = int(input())
d5 = int(input())

def num_petals(d1, d2, d3, d4, d5):
    sum = 0
    if d1 % 2 != 0:
        sum = sum + (d1 - 1)
    if d2 % 2 != 0:
        sum = sum + (d2 - 1)
    if d3 % 2 != 0:
        sum = sum + (d3 - 1)
    if d4 % 2 != 0:
        sum = sum + (d4 - 1)
    if d5 % 2 != 0:
        sum = sum + (d5 - 1)
    return sum

print(num_petals(d1,d2,d3,d4,d5))
