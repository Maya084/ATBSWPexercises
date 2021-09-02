import re

def primer(rec):
    pom = batRegex.search(rec)
    print("Recenica: "+ rec)
    print(f'mo.group() = {pom.group()}')
    print()



batRegex = re.compile(r'Bat(wo)*man')  #0 ili povekje pati wo ako se naogja pred man

rec1 = 'The Adventures of Batwoman' # 1 pojavuvanje na wo
rec2 = 'The Adventures of Batman' # 0 pojavuvanja na wo
rec3 = 'The Adventures of Batwowowowoman' #4 pojavuvanja na wo

primer(rec1)
primer(rec2)
primer(rec3)