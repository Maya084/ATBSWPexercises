import re

copRegex = re.compile(r'Police(wo)?man')

sentence = 'Policewoman and Policeman bad.'
found = copRegex.search(sentence)

print('The sentence is: "' + sentence +'"')

if found != None:
    print(f'Found word: {found.group()}')
    print(f'found.group(1) = {found.group(1)}')
else:
    print('Ne e pronajden zbor.')
