millier = list(range(100,1001))
okay = []
def zeub ():
    okay = []

    for position in millier :
        if (position % 7 == 0) :
            if (position % 5 !=0) and (position % 2 !=0):
                okay.append(position)
    return okay 


print (zeub())