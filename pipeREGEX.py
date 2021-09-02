import re

rec = "Lola i Tina otidoa na odmor."
new = re.compile(r'Tina|Mina|Lola')
ime = new.search(rec)

print(f'Recenica: {rec}')
print(f'group() = {ime.group()}')

#  ---------------------------------------------------
print()

batRegex = re.compile(r'Bat(man|mobile|copter|bat|)')
novarec = "Batman was found dead."

keyword = batRegex.search(novarec)
if keyword != None:
    print(f'Vo recenicata "{novarec}" pronajden e zborot {keyword.group()}')
    print(f'group(1) = {keyword.group(1)}')
else:
    print(f'Vo recenincata "{novarec}" ne e pronajden klucen zbor')
