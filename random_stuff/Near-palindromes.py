import string
alfa=string.ascii_lowercase
n = int(input())

def checker(parola):
    x=parola[::-1]
    if x==parola:
        return(True)
    else:
        return(False)

def rimuovi(parola):
    parole=[]
    i=0
    while i<len(parola):
        nuova_parola=''
        nuova_parola+=parola[:i]
        nuova_parola+=parola[i+1:]
        if checker(nuova_parola)==True:
            parole.append(nuova_parola)
        i+=1
    return parole

def sostituisci(parola,alfa):
    i=0
    parole_sostituite=[]
    while i<len(parola)//2:
        nuova_parola=list(parola)
        for l in alfa:
            nuova_parola[i]=l
            if checker(nuova_parola)==True:
                parole_sostituite.append("".join(nuova_parola))
        i+=1
    return parole_sostituite

s=''
for i in range(n):
    word=input()
    k=rimuovi(word)+sostituisci(word,alfa)
    if k:
        s+='1'
    else:
        s+='0'

print(s)