#!/usr/bin/env python3
#chapter 7 project
#phoneAndEmail.py - Finds phone number and email addresses on the clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(
     (\d{3}|\(\d{3}\))?             # area code
     (\s|-|\.)?                     # seperator
     (\d{3})                        # first 3 digit
     (\s|-|\.)                      #seperator
     (\d{4}|\(\d{4}\))              #last 4 digit
     (\s*(ext|x|ext.)\s(\d{2,5}))?  #extension
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       #username
    @                       #@ symbol
    [a-zA-Z0-9.-]+          #domain name
    (\.[a-zA-Z]{2,4})       #dot - something
    )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNumber = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNumber += ' x' + groups[8]
    matches.append(phoneNumber)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')