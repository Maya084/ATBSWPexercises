#! usr/bin/python
print("-------------------------------------------------------------")
print("---------------------POCETOK NA PROGRAMA---------------------")
print("-------------------------------------------------------------")

lista = list(range(1,6))
i = 0
while i<5:
    print(lista[i])
    i+=1
    
    
pom_lista=[5, 4, 3, 1, -2, -3, 5, -5]
total = 0
for element in pom_lista:
    if element<0:
        break
    total+=element
    
print("zbir na pozitivnite broevi na listata: "+str(pom_lista) + " e: "+str(total))

total2=0
i=0
while True:
    if pom_lista[i]<0:
        break
    total2 += pom_lista[i]
    i+=1

print("zbir na pozitivnite broevi na listata: "+str(pom_lista) + " presmetana so while e " + str(total2))

total3=0
novalista = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
pom = len(novalista)-1


while pom >= 0:
    if novalista[pom] >= 0:
        break
    else:
        total3 += novalista[pom]
        pom -= 1

print("\nzbir na negativnite elementi na listata: " + str(novalista) + " e: " + str(total3))
