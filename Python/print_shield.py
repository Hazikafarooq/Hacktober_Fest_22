def bend(char,size):
    
    for i in range(size):
        
        if i == 0 or i == size-1:
            print(size*f'{char} ')
            
        else:
            print(char + (2*i-1)*' ' + char + ((2*size-3) - 2*i)*' ' + char)
            
char = input('Enter your character: ')    
size = int(input('Enter the size of your shield: '))
bend(char,size)
