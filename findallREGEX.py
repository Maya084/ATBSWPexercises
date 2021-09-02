import re

def find(recenica):
    reg = re.compile(r'\d+\s\w+')
    a = reg.findall(recenica)
    print("List:")
    for i in range(len(a)):
        print(a[i])
    print()

find('I have 12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge and much more.')