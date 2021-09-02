import re

brojReg = re.compile(r'(\d{3})-(\d{3}-\d{3})')
recenica = 'Mojot domasen broj e 032-382-941,  a mobilniot e 078-357-145'
broevi = brojReg.findall(recenica)
for i, j in broevi:
    print(i)
    print(j)
    print(i + '-' + j)
    print()
    