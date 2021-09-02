import re

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{3}')
mo = phoneNumRegex.search("My number is 032-382-941.")
print("The found number: " + mo.group())

print()

newphRex = re.compile(r'(\d{3})-(\d{3}-\d{3})')
mo2 = newphRex.search("My number is 032-382-941.")
print(mo2.group())
print(mo2.group(1))
print(mo2.group(2))

print()

print("str(groups()): " + str(mo2.groups()))

print()

operator, broj = mo2.groups()

print("Broj na grad: " + operator)
print("Broj: " + broj)

print()

print(f"Broj na grad: {mo2.groups()[0]} izvrseno so groups()[0], broj: {mo2.groups()[1]} izvrseno so groups()[1]")

#------------------------------------------------------------

text = "Mojot broj e (032) 382-941."
new = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d)')
broj = new.search(text)

if broj != None:
    print(broj.group(1))
else:
    print("Nema broj vo tekstot")

