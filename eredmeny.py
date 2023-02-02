#megoldás
def eredmeny(jatekoslapok:list, geplapok:list):
    jatekospont = osszpont(jatekoslapok)
    geppont = osszpont(geplapok)

    if jatekospont > 21 and geppont > 21:
        return "mindenki vesztett"
    elif jatekospont > 21:
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
    jatekoslapok = [10,9,3]
    geplapok = [10,11]
    print(eredmeny(jatekoslapok, geplapok))
    
def gep_vesztett_teszt():
    jatekoslapok = [10,5,8]
    geplapok = [10,5, 10]
    print(eredmeny(jatekoslapok, geplapok))
    
def jatekos_nyert_teszt():
    jatekoslapok = [10,9]
    geplapok = [10, 7]
    vart = "jatekos nyert"
    kapott = eredmeny(jatekoslapok, geplapok)
    if vart == kapott:
        print("Teszteset sikeres.")
    else:
        print("Teszteset sikertelen.")


def gep_nyert_teszt():
    jatekoslapok = [10,7]
    geplapok = [10, 10]
    vart = "gep nyert"
    kapott = eredmeny(jatekoslapok, geplapok)
    if vart == kapott:
        print("Teszteset sikeres.")
    else:
        print("Teszteset sikertelen.")

def jatekos_nyert_lapszammal_teszt():
    jatekoslapok = [10, 9]
    geplapok = [10, 4, 5]
    vart = "jatekos nyert"
    kapott = eredmeny(jatekoslapok, geplapok)
    if vart == kapott:
        print("Teszteset sikeres.")
    else:
        print("Teszteset sikertelen.")


def gep_nyert_lapszammal_teszt():
    jatekoslapok = [10, 4, 5]
    geplapok = [10, 10]
    vart = "gep nyert"
    kapott = eredmeny(jatekoslapok, geplapok)
    if vart == kapott:
        print("Teszteset sikeres.")
    else:
        print("Teszteset sikertelen.")

def dontetlen_21_alatt_teszt():
    jatekoslapok = [10, 3, 5]
    geplapok = [10, 4, 4]
    vart = "dontetlen"
    kapott = eredmeny(jatekoslapok, geplapok)
    if vart == kapott:
        print("Teszteset sikeres.")
    else:
        print("Teszteset sikertelen.")

def tesztek():
    jatekos_vesztett_teszt()
    gep_vesztett_teszt()


tesztek()

