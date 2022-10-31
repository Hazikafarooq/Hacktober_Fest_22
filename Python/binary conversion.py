n = int(input())

def binary_string(num):
    if(num == 1):
        return("1")
    if(num == -1):
        return("-1")
    elif(num == 0):
        return("0")
    elif(num<0):
        num = num * -1
        ans = (str(binary_string(num//2)) + str(num%2))
        return("-"+ans)
    else:
        ans = (str(binary_string(num//2)) + str(num%2))
        return(ans)