size = input ("De quelle taille souhaites-tu que ton sapin soit ?\n")
size =  int(size)
for level in range (size) :
    print (" "*(int(size)-int(level)-1)+"*"*(2*level +1 ))
print (" "*(int(size)-2)+"#"*2)

 