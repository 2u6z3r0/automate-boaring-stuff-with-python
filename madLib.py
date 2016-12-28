#!/usr/bin/env python3
# madLib.py - Replaces ADJECTIVE, NOUN, ADVERB, VERB with user input

import re, os, sys


def usage():
    print('Usage: madLib.py <file_name>')

madLibRegex = re.compile(r'(ADJECTIVE)|(NOUN)|(ADVERB)|(VERB)')

if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        inputFile = open(sys.argv[1])
        outputFile = open('madLibOutput.txt', 'w')
        for line in inputFile.readlines():
            newLine = ''
            for word in line.split():
                mo = madLibRegex.search(word)
                if mo:
                    print('Enter {}'.format(mo.group()))
                    replaceText = input()
                    word = madLibRegex.sub(replaceText, word)
                newLine += ' ' + word
            outputFile.write(newLine)
            print(newLine)

        inputFile.close()
        outputFile.close()
    else:
        print('please specify correct filename')
        usage()
else:
    usage()