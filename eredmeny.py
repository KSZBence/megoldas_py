#megoldás
def eredmeny(jatekoslapok:list, geplapok:list):
    jatekospont = osszpont(jatekoslapok)
    geppont = osszpont(geplapok)
    jatekosdb = len(jatekoslapok)
    gepdb = len(geplapok)

    if jatekospont <= 21 and geppont <= 21:
        if jatekospont > geppont:
            vegeredmeny = "Jatekos nyert"
        elif geppont > jatekospont:
            vegeredmeny = "Gep nyert"
        elif geppont == jatekospont:
            if jatekosdb < gepdb:
                vegeredmeny = "Jatekos nyert"
            elif jatekosdb > gepdb:
                vegeredmeny = "Gep nyert"
            else:
                vegeredmeny = "Döntetlen"
    else:
        if jatekospont > 21:
            vegeredmeny = "Jatekos vesztett"
        if geppont > 21:
            vegeredmeny = "Gep vesztett"
        if jatekospont > 21 and geppont > 21:
            vegeredmeny = "Döntetlen"


    return vegeredmeny
    


    # if jatekospont > 21 and geppont > 21:
    #     return "dontetlen"
    # elif jatekospont > 21:
    #     return "jatekos vesztett"
    # elif geppont > 21:
    #     return "gep vesztett"
    
    


def osszpont(lista) -> int:
    osszeg = 0
    for i in lista:
        osszeg += i
    return osszeg



#teszteset

def jatekos_vesztett_teszt():
    jatekoslapok = [10,9,3]
    geplapok = [10,11]
    vart = "Jatekos vesztett"
    kapott = eredmeny(jatekoslapok, geplapok)
    if vart == kapott:
        print("Teszteset sikeres.")
    else:
        print("Teszteset sikertelen.")
    
def gep_vesztett_teszt():
    jatekoslapok = [10,8]
    geplapok = [10,5, 10]
    vart = "Gep vesztett"
    kapott = eredmeny(jatekoslapok, geplapok)
    if vart == kapott:
        print("Teszteset sikeres.")
    else:
        print("Teszteset sikertelen.")
    
def mindenki_vesztett_dontetlen_teszt():
    jatekoslapok = [10,9,5]
    geplapok = [10, 8, 5]
    vart = "Döntetlen"
    kapott = eredmeny(jatekoslapok, geplapok)
    if vart == kapott:
        print("Teszteset sikeres.")
    else:
        print("Teszteset sikertelen.")
    
def jatekos_nyert_teszt():
    jatekoslapok = [10,9]
    geplapok = [10, 7]
    vart = "Jatekos nyert"
    kapott = eredmeny(jatekoslapok, geplapok)
    if vart == kapott:
        print("Teszteset sikeres.")
    else:
        print("Teszteset sikertelen.")


def gep_nyert_teszt():
    jatekoslapok = [10,7]
    geplapok = [10, 10]
    vart = "Gep nyert"
    kapott = eredmeny(jatekoslapok, geplapok)
    if vart == kapott:
        print("Teszteset sikeres.")
    else:
        print("Teszteset sikertelen.")

def jatekos_nyert_lapszammal_teszt():
    jatekoslapok = [10, 9]
    geplapok = [10, 4, 5]
    vart = "Jatekos nyert"
    kapott = eredmeny(jatekoslapok, geplapok)
    if vart == kapott:
        print("Teszteset sikeres.")
    else:
        print("Teszteset sikertelen.")


def gep_nyert_lapszammal_teszt():
    jatekoslapok = [10, 4, 5]
    geplapok = [10, 9]
    vart = "Gep nyert"
    kapott = eredmeny(jatekoslapok, geplapok)
    if vart == kapott:
        print("Teszteset sikeres.")
    else:
        print("Teszteset sikertelen.")


def dontetlen_21_alatt_teszt():
    jatekoslapok = [10, 3, 5]
    geplapok = [10, 4, 4]
    vart = "Döntetlen"
    kapott = eredmeny(jatekoslapok, geplapok)
    if vart == kapott:
        print("Teszteset sikeres.")
    else:
        print("Teszteset sikertelen.")


def tesztek():
    jatekos_vesztett_teszt()
    gep_vesztett_teszt()
    mindenki_vesztett_dontetlen_teszt()
    jatekos_nyert_teszt()
    gep_nyert_teszt()
    jatekos_nyert_lapszammal_teszt()
    gep_nyert_lapszammal_teszt()
    dontetlen_21_alatt_teszt()    
    
    


tesztek()

