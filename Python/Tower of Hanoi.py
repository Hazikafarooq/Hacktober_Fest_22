#peg0 is source
#peg1 is other
#peg2 is destination
select = int(input())



def count_hanoi_moves(n): #select == 1
    if n == 0:
        return 0
    else:
        print((2**n)-1)
    
def hanoi_moves(n, src, dst): #select == 2
    #prints each move
    other = 3 - (src + dst)
    if n == 0:
        return
    else:
        hanoi_moves(n-1, src, other)
        print('Move disk from peg', src, 'to peg',dst)
        hanoi_moves(n-1, other, dst)

if select == 1:
    n = int(input())
    count_hanoi_moves(n)
if select == 2:
    n = int(input())
    src = int(input())
    dst = int(input())
    hanoi_moves(n, src, dst)

    

   
   
    

import inspect
func = hanoi_moves
source = inspect.getsource(func)
if "for " in source or "while " in source or func.__name__ not in source:
  print("Try a recursive approach!")
else:
  func = count_hanoi_moves
  source = inspect.getsource(func)
  if "for " in source or "while " in source or func.__name__ not in source:
      print("Try a recursive approach!")