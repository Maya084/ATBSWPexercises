import re

def printanje(rec):
    mo = batRegex.search(rec)
    print(f'Recenica : {rec}')
    if mo != None:
        print(f'mo.group() = {mo.group()}')
    else:
        print("Ne e pronajdeno nisto.")
    
    print()
        
    
batRegex = re.compile('Bat(wo)+man')

rec1 = 'The Adventures of Batwoman' # 1 pojavuvanje na wo
rec2 = 'The Adventures of Batman' # 0 pojavuvanja na wo
rec3 = 'The Adventures of Batwowowowowoman'  #5 pojavuvanja na wo

printanje(rec1)
printanje(rec2)
printanje(rec3)