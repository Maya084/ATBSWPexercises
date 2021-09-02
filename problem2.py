def string_times (zbor, broj):
    print(broj*zbor)
    
b=5
zbor="Hello "
string_times(zbor,b)

def string_times_for(zbor,broj):
    for i in range(0, broj):
        print(zbor)
        

def string_times_while(zbor,broj):
    i=0
    while i<broj:
        print(zbor)
        i+=1
        

string_times_for("for", 7)
string_times_while("while", 3)


def hello(name):
    return "Hello " + name

print(hello("Bob"))
