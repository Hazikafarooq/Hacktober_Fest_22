def days_to_cover(lily):
    if lily <= 1:
        return(0)
    else:
        ans = (days_to_cover(lily/2)+1)
        return(int(ans))