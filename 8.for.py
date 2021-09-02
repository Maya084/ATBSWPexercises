#! usr/bin/python
print("----------POCETOK NA PROGRAMA-----------")
lista=["banana", "apple", "microsoft"]
for element in lista:
    print (element)
    
b=[5,4,6,7,3,2,5]
print(b)
print("zbir na elementi na b")
pom = 0
for elem in b:
    pom = pom + elem
    
print(pom)

pom2=0

for elem in range(1,5):
    pom2=pom2+elem

print("zbir na range(1,5) e: ")
print (pom2)

pomosna_lista=list(range(1,8))
print(pomosna_lista)

total3 = 0
for i in pomosna_lista:
    if i % 3 == 0:
        total3 += i

print(total3)

print()
print("zbir na site broevi od 1 do 100 dellivi so 3 i 5")
zbir=0
for i in range(1,100):
    if (i%3 == 0) & (i%5==0):
        zbir+=i

print(zbir)
