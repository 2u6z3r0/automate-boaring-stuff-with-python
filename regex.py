#!/usr/bin/env python3
#chapter 7 examples all in a single file
import re

# \d - numeric digit 0-9
# \D - any character that is not a numeric digit 0-9
# \w - any letter, digit, or the underscore charecter
# \W - any character that is not letter, digit, underscore
# \s - any space,tab, or new line character
# \S - any character this is not space,tab,new line character
# . - matches anycharacter, except newline character
# ? - 0 or 1 isinstance matching
# * - 0 or more isinstance
# + - 1 or more instance
# {2,4} - repeat 2 to 4 times, greedy matching - means matches the longest string. ex-(ha){2,4} matches 'hahahaha'
# {2,4}? - repeat 2 to 4 times, but its non-greedy matching - means matches the shortest string. ex-(ha){2,4} matches 'haha'
# [aeAE] - custom character class, matches all the character specified within []
# [^aeAE] - matches all the characters other than the character specified within []
# ^ab - matches to 'ab' at the beginning of the search text
# ab$ - matches to text ending with ab at the end of the matching text



# phoneNumRegex = re.compile('\d\d\d\-\d\d\d-\d\d\d\d')
phoneNumRegex = re.compile('(\d\d\d)-(\d\d\d-\d\d\d\d)') #to group certain text use paranthesis
mo = phoneNumRegex.search('My phone number is 444-123-6789')
print('Phone number found - ',mo.group())
print(mo.groups())
print('Area code is - ', mo.group(1))
print(mo.group(2))
areaCode, mainNumber = mo.groups() #mo.groups returns a tuple of values, use simple trick to assign
                                    # tuple values to multiple vars at once
print('area code - ', areaCode)
print('main number', mainNumber)

#matching multiple groups
heroRegex = re.compile(r'Batman|Tina Fey') # '|' is used to match multiple groups
                                            #Here its matches either 'Batman' or 'Tina Fey'

#matching multiple groups - 2
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())  #mo.group() returns all the matched text 'Batmobile'
print(mo.group(1)) #mo.group(1) returns just the part of the matched text inside the first parenthesis group 'mobile'

#optional matching with the ? example
print('mathcing using ?')
batRegex = re.compile(r'Bat(wo)?man') #here (wo)? pattern matches 'wo' optionally
mo = batRegex.search('The Adventures of Batman')
print(mo.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

print('matching using ?')
phoneNumRegex = re.compile('(\d\d\d-)?(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is 123-6789')
print('Phone number found - ', mo.group())

print('matching using *')
batRegex = re.compile(r'Bat(wo)*man') #here (wo)? pattern matches 'wo' optionally
mo = batRegex.search('The Adventures of Batwowowoman')
print(mo.group())

# + matches 1 or more instances
print('mathcing using +')
batRegex = re.compile(r'Bat(wo)+man') #here (wo)? pattern matches 'wo' optionally
mo = batRegex.search('The Adventures of Batwowowowowoman')
print(mo.group())
mo = batRegex.search('The Adventures of Batman')
if mo != None:
    print(mo.group())   #throws AttributeError as it donesnt match specified pattern

haRegex = re.compile('(ha){2}') #matches to 'ha' repeated 2 times i.e 'haha'
mo = haRegex.search('hahahahahaha')
print(mo.group())

haRegex = re.compile('(ha){2,4}') #matches to 'ha' repeated 2 to 4 times i.e 'haha', 'hahaha', 'hahahaha'
mo = haRegex.search('hahahahahaha') #matches the 'hahahaha' as its greedy-matching
print(mo.group())

haRegex = re.compile('(ha){2,4}?') #matches to 'ha' repeated 2 to 4 times i.e 'haha', 'hahaha', 'hahahaha'
mo = haRegex.search('hahahahahaha') #matches the 'haha' as its greedy-matching
# print(type(mo))            #just for curiosity i checked return type of haRegex.search, and its of type '_sre.SRE_Match'
print(mo.group())

phoneNumRegex = re.compile('(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000') #findall returns tuple, and its items are the matched strings for each group in the regex