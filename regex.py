import re

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

heroRegex = re.compile(r'Batman|Tina Fey') # '|' is used to match multiple groups
                                            #Here its matches either 'Batman' or 'Tina Fey'
