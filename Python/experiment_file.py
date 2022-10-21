word = input()
word = word.replace(" ","")

def center_pos(word):
    
    if len(word)%2 != 0:
        return (len(word)//2)+1
    else:
        return str(len(word)//2) + 'and' + str((len(word)//2)+1)
      
print(center_pos(word))
