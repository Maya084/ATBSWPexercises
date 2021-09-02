#! usr/bin/python

def bmi (name, height, weight):
    bminum = weight / height**2
    print(name + " has a BMI of " + str(bminum))
    if bminum >= 25.0:
        print(name + " is overweight")
    elif (bminum < 25.0) & (bminum >= 18.0):
        print(name + " has a normal weight")
    else:
        print(name + " is underweight")
        
name1=str(input("Enter name: "))
weight1 = float(input("Enter weight: "))
height1 = float(input("Enter height: "))
bmi(name1, height1, weight1)
