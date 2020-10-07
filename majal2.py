
class Edo :
    def __init__ ( self , nombre , padre , f ) :
        self . nombre = nombre
        self . padre = padre
        self . f = f


def miembro ( edo , lista ) :
    resp = False
    indi = -1
    cuenta =0
    for nodo in lista :
        if edo == nodo . nombre :
            resp = True
            indi = cuenta
            break
        else :
            cuenta = cuenta +1
    return resp , indi

def expandir ( edo , proble , Abiertos , Cerrados ) :
    hijos = proble [ edo . nombre ]
    for hijo in hijos :
        fnue = edo . f + hijos [ hijo ]
        m , p = miembro ( hijo , Cerrados )
        if not m :
            m2 , p2 = miembro ( hijo , Abiertos )
            if m2 :
                fori = Abiertos [ p2 ]. f
                if fnue < fori :
                    Abiertos [ p2 ]= Edo ( hijo , edo . nombre , fnue )
            else :
                Abiertos . append ( Edo ( hijo , edo . nombre , fnue ) )
    return Abiertos

def siguiente ( Abiertos ) :
    fmejor =100
    mejor = None
    donde =0
    cuenta =0
    for nodo in Abiertos :
        if nodo .f < fmejor :
            fmejor = nodo . f
            mejor = nodo
            donde = cuenta
        cuenta = cuenta +1
    del Abiertos [ donde ]
    return Abiertos , mejor

def primMej ( ini , meta , proble ) :
    Abiertos =[ Edo ( ini , ini ,0) ]
    Cerrados =[]
    listo = False
    while not listo :
        Abiertos , actual = siguiente ( Abiertos )
        if actual . nombre == meta :
            listo = True
            Cerrados . append ( actual )
        else :
            Cerrados . append ( actual )
            Abiertos = expandir ( actual , proble , Abiertos , Cerrados )
    return Cerrados

def getCamino ( ini , Cerrados ) :
    resp =[]
    listo = False
    actual = Cerrados [ -1]. nombre
    while not listo :
        if actual == ini :
            listo = True
            resp . insert (0 , actual )
        else :
            for nodo in Cerrados :
                if nodo . nombre == actual :
                    resp . insert (0 , actual )
                    actual = nodo . padre
                    break
    return resp

 ## Esto es la funcion principal
def main(ini,meta) :
    proble ={ 
        'A':{ 'B':5 , 'C':8, 'D':7,'E':13,'F':32,'G':18} ,
        'B':{ 'A':5 , 'C':9 , 'D':14,'E':8,'F':35,'G':19} ,
        'C':{ 'A':8 , 'B':9 , 'D':6 , 'E':7,'F':26,'G':8},
        'D':{ 'A':7 ,'B':14, 'C':6 ,'E':16, 'F':27,'G':12} ,
        'E':{ 'A':13,'B':8 , 'C':7 , 'D':16,'F':35,'G':15} ,
        'F':{ 'A':32,'B':35,'C':26,'D':27 , 'E':35,'G':15},
        'G':{ 'A':18,'B':19,'C':8,'D':12,'E':15,'F':15}
    }
    cerrados = primMej ( ini , meta , proble )
    camino = getCamino ( ini , cerrados )
    print ('Solucion prmero por lo mejor: ')
    print ( camino )

if __name__ == '__main__':

    n1=input("Ingresa el estado inicial: ")
    n2=input("Ingrese el estado final: ")
    main (n1,n2)
