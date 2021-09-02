def count_evens(niza):
    brojac=0
    for each in niza:
        if each%2 == 0:
            brojac+=1
    
    return brojac
            
niza=list(range(1,50))
print("Broj na parni broevi od 1 do 49 e: "+ str(count_evens(niza)))
