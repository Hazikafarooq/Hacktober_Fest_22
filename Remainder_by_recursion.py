a = int(input())
b = int(input())

def modulus(a,b):
    
    if a < b:
        return a
       
    return modulus(a-b,b)
  
  print (modulus(a,b))
