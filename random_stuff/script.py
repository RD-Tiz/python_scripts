#gioco del tris di gesu crist
import sys

grid=[
        [1,2,3],
        [4,5,6],
        [7,8,9],
     ]

def printa_giuoco(m):
    c=0
    for i in m:
        s=''
        c+=1
        for l in i:
            s+=(" | %s |" % str(l))
        if c!=len(m):
            s+="\n-------------------"
        else:
            s+="\n"
        print(s)

def riempi_casella(m,n,player):
    d=0
    for i in m:
        c=0
        while c<len(i):
            if i[c]==n:
                i[c]=player
                d+=1
            c+=1
    if d==1:
        return(m)
    else:
        return(1)

def check_hor(m):
    for i in m:
        x=set(i)
        if len(x)==1 and "X" in x:
            return(0)
        elif len(x)==1 and "O" in x:
            return(1)

def check_vert(m):
    j=0
    while j<len(m):
        c=0
        d=0
        i=0
        while i<len(m):
            if m[i][j]=="O":
                c+=1
            elif m[i][j]=="X":
                d+=1
            if d==3:
                return(0)
            if c==3:
                return(1)
            i+=1

        j+=1

def check_dia(m):
    c=0
    g=0
    d=0
    for i in range(0,len(m)):
        if m[i][c]=="O":
            d+=1
        elif m[i][c]=="X":
            g+=1
        c+=1
    if d==3:
        return(1)
    elif g==3:
        return(0)
    
def check_dia2(m):
    c=len(m)-1
    g=0
    d=0
    i=0
    while c>=0:
        if m[i][c]=="O":
            d+=1
        elif m[i][c]=="X":
            g+=1
        i+=1
        c-=1
    if d==3:
        return(1)
    elif g==3:
        return(0)

def draw(m):
    size=(len(m))*(len(m[0]))
    c=0
    for i in m:
        for l in i:
            if l=="X" or l=="O":
                c+=1
    if c==size:
        return(True)
    else:
        return(False)



input("Benvenuti al gioco del tris di jesu crist, premere invio per continuare\n")
input("Giocatore 1 inserirai degli O\n")
input("Giocatore 2 inserirai degli 1\n\n\n")
while True:
    c=0
    g=0
    while c<1:
        printa_giuoco(grid)
        f=int(input("Giocatore O, scegli il numero della casella:\n"))
        if riempi_casella(grid,f,"O")!=1:
            c+=1
            printa_giuoco(grid)
        else:
            print("Errore, inserire numero valido\n")
            printa_giuoco(grid+"\n")
        if check_hor(grid)==1 or check_vert(grid)==1 or check_dia(grid)==1 or check_dia2(grid)==1:
            print("Il giocatore O ha vinto")
            sys.exit()
        elif draw(grid)==True:
            print("Pareggio")
            print(printa_giuoco(grid))
            g+=1
            c+=1
    while g<1:
        d=int(input("Giocatore X, scegli il numero della casella\n"))
        if riempi_casella(grid,d,"X")!=1:
            g+=1
            printa_giuoco(grid)
        else:
            print("Errore, inserire numero valido\n")
            printa_giuoco(grid+"\n")
        if check_hor(grid)==0 or check_vert(grid)==0 or check_dia(grid)==0 or check_dia2(grid)==0:
            print("Il giocatore X ha vinto")
            printa_gioco(grid)
            sys.exit()
        elif draw(grid)==True:
            print("Pareggio")
            print(printa_giuoco(grid))
            g+=1
            c+=1
       
