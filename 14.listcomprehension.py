a=[1,5,10,15]
a.append(20)
a.append(25)
a.append(30)
a.pop()
b=[]

for i in range (len(a)):
    b.append(3*a[i])

print(a)
print(b)

c=[i*2 for i in a]
print(c)

d=[i**2 for i in range(1,7)]
print(d)

e=[x**2 for x in range(6,0, -1)]
print (e)
