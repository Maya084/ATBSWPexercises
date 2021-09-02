import re

samoglaski = re.compile(r'[^aeiouAEIOU0-9\.\!\?\_\,\s\-\[\]]')

tekst = "You can also include ranges of letters or numbers by using a hyphen. For example, the character class [a-zA-Z0-9] will match all lowercase letters,uppercase letters, and numbers."

listaSamoglaski = samoglaski.findall(tekst)
listaEdincecni = []
for i in range(len(listaSamoglaski)):
    if listaSamoglaski[i] in listaEdincecni:
        continue
    else:
        listaEdincecni+=listaSamoglaski[i]

print(listaEdincecni)