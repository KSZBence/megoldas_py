#megoldás
def eredmeny(jatekoslapok:list, geplapok:list):
    jatekospont = osszpont(jatekoslapok)
    geppont = osszpont(geplapok)

    if jatekospont > 21:
        return "jatekos vesztett"
    elif geppont > 21:
        return "gep vesztett"


def osszpont(lista) -> int:
    osszeg = 0
    for i in lista:
        osszeg += i
    return osszeg



#teszteset

def jatekos_vesztett_teszt():
    jatekoslapok = [10,10,2]
    geplapok = [10,11]
    print(eredmeny(jatekoslapok, geplapok))

def tesztek():
    jatekos_vesztett_teszt()


tesztek()