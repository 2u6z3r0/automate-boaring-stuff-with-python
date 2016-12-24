#!/usr/bin/env python3
#pwd.py An insecure password manager, its copies specified account password to clip board if account exsists
import sys, pyperclip

passwords ={'email': 'emailpassword',
            'facebook': 'Facebook password',
            'Twitter': 'Twiter password'
            }

if len(sys.argv) < 2:
    print('Usage : pwd.py [account]')
    sys.exit()

account = sys.argv[1]
if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for {} is copied to clipboard'.format(account))
else:
    print('there is no account named ' + account)
