class Robot:
    
    def __init__(self, name, color, weight):
        self.name=name
        self.color=color
        self.weight=weight
        
    def introduce_self(self):
        print("My name is " + self.name)
        
        
        
class Person:
    def __init__(self, name, personality, isSitting):
        self.name=name
        self.personality=personality
        self.isSitting = isSitting
    
    def sit_down(self):
        self.isSitting=True
    
    def stand_up(self):
        self.isSitting=False
        
#########################################################

r1=Robot("Tom", "red", 30)
r2=Robot("Jerry", "blue", 40)

p1=Person("Alice", "aggressive", False)
p2=Person("Becky", "talkative", True)

p1.robotOwned=r2
p2.robotOwned=r1


print("Person 1's robot: ")
p1.robotOwned.introduce_self()

print("Person 2's robot: ")
p2.robotOwned.introduce_self()


"""
r1.introduce_self()
r2.introduce_self()
"""
