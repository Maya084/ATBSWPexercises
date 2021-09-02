#! usr/bin/python

def mile_to_kilometar(mile):
    return mile*1.6

mile=float(input("Enter miles: "))
print(str(mile) + " miles is " + str(mile_to_kilometar(mile)) + " kilometars")
