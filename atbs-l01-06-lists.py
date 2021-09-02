def a():
    print("-------------------------")

m = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(0, 10):
    print(str(m[i]) + " * " + str(m[9 - i]) + " = " + str(m[i] * m[9 - i]))
    
a()
for i in m:
    print(i)

a()
print(m)

a()
pr = ['eden', 'dva', 'tri']
eden, dva, tri = pr
print(eden)
print(dva)
print(tri)

a()
lista = ["maja", "gordana", "MAJA", "Marija", "Tom", "happy", "Peter", "snoopy"]
print("Lista:")
print(lista)
print()
lista.sort(reverse = False, key=str.lower)
print("Sortirana:")
print(lista)

a()
lista2 = [1, 2, 3, 4, 6, 23, 5, 54645, 2, 4, -9, 24, -6, 13, 87]
print(lista2)
lista2.sort(reverse=True)
print(lista2)
