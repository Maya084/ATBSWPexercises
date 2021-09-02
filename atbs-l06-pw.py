#! python3
# Insecure password locker program

import sys, pyperclip

PASSWORDS = { 'email' : 'MajaN',
              'blog' : 'MarijaN',
              'youtube' : 'Random012'}

if len(sys.argv)<2:
    print('Usage: python atbs-l06-pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(f"Password for {account} copied to clipboard.")
else:
    print(f"There is no account named {account}.")
