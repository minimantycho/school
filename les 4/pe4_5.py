def kwadraten_som(grondgetallen):
    getal = 0
    for plus in grondgetallen:
        if plus >= 1:
            getal = getal + (plus* plus)
    return(getal)
cijfers = [4,5,3,-81]
print(kwadraten_som(cijfers))