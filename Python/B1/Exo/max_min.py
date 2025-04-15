salaire = [2000,1345,1116,63683,5373,387363,272,398397,39733,397303]

def max_min (liste):
    max = liste[0]
    min = liste[0]

    for position in liste :
        if position > max :
            max = position 
        if position < min :
            min = position 
    return min,max

print(max_min(salaire))


        