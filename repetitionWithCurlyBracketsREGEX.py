import re

def testgreedy(rec):
    reg = re.compile(r'(Ha){3,7}') #3 pati minimum, 7 pati max
    mo = reg.search(rec)
    
    print("Primer (greedy): " + rec)
    if mo != None:
        print("Found: " + mo.group())
    else:
        print("Did not find anything")
    
    print()

def testnotgreedy(rec):
    reg = re.compile(r'(Ha){3,7}?') #3 pati minimum, 7 pati max, vrakja minimum
    mo = reg.search(rec)
    
    print("Primer (not greedy): " + rec)
    if mo != None:
        print("Found: " + mo.group())
    else:
        print("Did not find anything")
    
    print()

rec1 = 'JAs se smeev HaHAHaHaHa '
rec2 = 'Ti se smeese HaHa '
rec4 = 'Taa se smeese HaHaHaHaHaHaHa '
rec3 = 'Toj se smeese HaHaHaHaHaHaHaHaHaHaHaHa '
rec5 = 'Site se smeevme HaHaHa '

testgreedy(rec1)
testnotgreedy(rec1)

testgreedy(rec2)
testnotgreedy(rec2)

testgreedy(rec3)
testnotgreedy(rec3)

testgreedy(rec4)
testnotgreedy(rec4)

testgreedy(rec5)
testnotgreedy(rec5)

