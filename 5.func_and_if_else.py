#! usr/bin/python

def pogolem (x, y):
    if x>y:
        print(str(x)+" is greater than "+ str(y))
    elif x==y:
        print(str(x)+" is equal to "+str(y))
    else:
        print(str(x) + " is not greater than " + str(y))
        
x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))

pogolem(x,y)
