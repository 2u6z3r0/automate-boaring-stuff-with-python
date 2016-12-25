#/usr/bin/env python3
#chapter 7 practice project-2

import re

rstripRegex = re.compile(r'^\s+')
lstripRegex = re.compile(r'\s+$')

def regStrip(text, char = None):
    if char != None:
        text = re.sub(r'^{}+'.format(char), '', text)
        text = re.sub(r'{}+$'.format(char), '', text)
    else:
        newText = rstripRegex.sub('-', text)
        text = lstripRegex.sub('-', newText)
    print(text)

print('Enter the text')
userText = str(input())
print('which character you want to strip : ')
char = str(input())
for text in userText.split(r'\n'):
    regStrip(text, char)
