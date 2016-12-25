#!/usr/bin/env python3
#chapter 7 exercise

import re

spclChar = re.compile(r'[!@#$%^&*]+')
capLetter = re.compile(r'[A-Z]+')
smallLetter = re.compile(r'[a-z]+')
digit = re.compile(r'[0-9]+')

while True:
    print('Enter a strong password')
    text = str(input())
    try:
        spcl = spclChar.findall(text)
        cap = capLetter.findall(text)
        small = smallLetter.findall(text)
        num = digit.findall(text)
    except:
        pass

    if len(text) > 7 and spcl and cap and small and num:
        print(text + ' is a strong password.')
        break
    else:
        print(text + ' is not a strong password, Try again')

print('completed')