a="Maja"
b=12
c=11.5
d=True

pogolem= b>c

if pogolem:
    print("B e pogolemo od C")
else:
    print("B ne e pogolemo od C")

if type(a)== str:
    print(str(type(a)))
    

def are_you_sad (is_rainy, has_umbrella):
    return is_rainy and not has_umbrella



if are_you_sad(True, True):
    print("You are sad")
else:
    print("You aren't sad")
    
    
    
def c_greater_thand_d_plus_e(c,d,e):
    return c> (d+e)

print("Vnesi c, d i e")
c=int(input())
d=int(input())
e=int(input())

if c_greater_thand_d_plus_e(c,d,e):
    print("True lol")
else:
    print("False yo")
