import re

atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))
print()

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.groups())

nongreedyRegex = re.compile(r'<.*?>')
print()
print('Recenica: <To serve man> for dinner.> ')
print("Non greedy: ")
mo = nongreedyRegex.search('<To serve man> for dinner.> ')
print(mo.group())

print()
print("Greedy: ")
greedyRegex = re.compile(r'<.*>')
mo2 = greedyRegex.search('<To serve man> for dinner.>')
print(mo2.group())