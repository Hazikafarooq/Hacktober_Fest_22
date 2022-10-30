def grains_placed(n):
    if n ==1: 
        return(1)
    else:
        ans=(grains_placed(n-1)*2+1)
        return(ans)