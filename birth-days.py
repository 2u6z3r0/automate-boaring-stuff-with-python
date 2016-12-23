#!/usr/bin/env python3
# This is a simple programm to demonstrate dictionary

birthdays = {'vitthal': 'June 2', 'bob': 'apr 1', 'sai': 'aug 12'}

while True:
    print('Enter the name: (blank to quit)')
    name = input()

    if name == '':
        break

    if name in  birthdays:
        print('{} is the birthday of {}'.format(birthdays[name], name))
    else:
        print('I dont have you birthday information of {}'.format(name))
        print('Enter your birthday')
        birthday = input()
        birthdays[name] = birthday
        print('birthday database updated')

print('see you again')