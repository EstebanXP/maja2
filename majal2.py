
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
    proble ={ 'A':{ 'B':5 , 'C':4.2 , 'D':5.6} ,
    'B':{ 'A':5 , 'C':4.5 , 'E':9.2} ,
    'C':{ 'A':4.2 , 'B':4.5 , 'D':2.7 , 'E':9.4} ,
    'D':{ 'A':5.6 , 'C':2.7 , 'F':12.2} ,
    'E':{ 'B':9.2 , 'C':9.4 , 'F':8.3} ,
    'F':{ 'D':12.2 , 'E':8.3}}
    cerrados = primMej ( ini , meta , proble )
    camino = getCamino ( ini , cerrados )
    print ('Solucion prmero por lo mejor: ')
    print ( camino )

if __name__ == '__main__':
    main ('A','F')
