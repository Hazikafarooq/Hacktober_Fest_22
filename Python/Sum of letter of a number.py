# Enter your code here.
n = int(input())
 
def sum_digits(n):
   if n == 0:
       return n
   else:
       temp = n % (10)
       n = n // (10)
       return temp + sum_digits(n)
      
      
import inspect
source = inspect.getsource(sum_digits)
if '[' in source:
 print('Do not convert to string!')
elif 'for' in source or 'while' in source:
 print('Try to solve the problem recursively!')
else:
 print(sum_digits(n))
