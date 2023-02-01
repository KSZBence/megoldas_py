#megoldás
def eredmeny(jatekospont, geppont):
    jatekospont = osszpont(jatekospont)
    geppont = osszpont(geppont)

    if jatekospont > 21:
        print("vesztettél")
    elif geppont > 21:
        print("nyertél")
#teszteset

def osszpont(lista):
    osszeg = 0
    for i in lista:
        osszeg += i
    return osszeg