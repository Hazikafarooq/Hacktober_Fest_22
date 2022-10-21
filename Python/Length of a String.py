# Enter your code here.
def length(s):
    count = 0
    for i in s:
        count += 1
    return(count)

s = input()

print(length(s))