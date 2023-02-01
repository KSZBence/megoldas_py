#megoldás
def eredmeny(jatekoslapok, geplapok):
    jatekospont = osszpont(jatekoslapok)
    geppont = osszpont(geplapok)

    if jatekospont > 21:
        print("vesztettél")
    elif geppont > 21:
        print("nyertél")


def osszpont(lista):
    osszeg = 0
    for i in lista:
        osszeg += i
    return osszeg

#teszteset