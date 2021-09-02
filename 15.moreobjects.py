class Person:
    def __init__(self, name, lastname, age):
        self.name=name
        self.lastname=lastname
        self.age=age
        
    def is_happy(self):
        return self.is_happy
    
    def retage(self):
        return self.age
    
    def isolder(self, a):
        return self.age>a.age
    
################################################

p1=Person("Maja", "Nikolovska", 20)
p2=Person("Marija","Nikolovska", 17)
p3=Person("Gordana","Kasapovska",59)

if p1.isolder(p3):
    print("Maja e postara od Gordana")
else:
    print("Maja ne e postara od Gordana")
