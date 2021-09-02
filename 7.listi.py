#! usr/bin/python

a=[3,10,-1]
print (a)
a.append(1)
print (a)
a.append("hello")
print(a)
a.append([7,8])
print(a)
a.pop()
print("used pop method")
print(a)
print("prv element: " + str(a[0]))
print("promenenp ptv element. niza: ")
a[0]=57
print(a)

b = ["banana", "apple", "microsoft"]
print("-----------------------\nlista b:")
print(b)
pom = b[0]
b[0]=b[2]
b[2]=pom
print("so promeneti prva i treta vrednost listata b e:")
print (b)
b[0] , b[2] = b[2] , b[0]
print("povtorna promena")
print(b)
