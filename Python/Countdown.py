# Enter your code here.
a = int(input())
b = int(input())
 

def countdown2(a,b):
   if a > b:
       if a == b:
           print(str(b))
       else:
           print(str(a), end = ", ")
           countdown2(a-1,b)
   elif b > a :
       print(str(b), end = ", ")
       countdown2(b-1, a)
   else:
       print(a) 
 
import inspect
source = inspect.getsource(countdown2)
if 'for' in source or 'while' in source:
 print('Try to solve the problem recursively!')
else:
 countdown2(a,b)
