def gcd(a, b):
    if b == 0: #Returns a when b = 0
        return a
    elif a == 0: #Returns b when a = 0
        return b
    else:
        return gcd(b, a % b) #Calls the function, switching the places of a and b, but also passes the remainder of a/b as 'b' to the new function

# Enter your code here.
a = int(input())
b = int(input())

import inspect
source = inspect.getsource(gcd)
if "for " in source or "while " in source:
  print("Try a recursive approach!")
else:
  result = gcd(a,b)
  if isinstance(result, int):
    print(result)
  else:
    print('Returned value is not an integer.')