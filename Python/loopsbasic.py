def max_char(n):
    max = '0'
    for x in n:
        if x > max:
            max = x 
    return max
    
print(max_char('5498753'))
