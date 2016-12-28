#!/usr/bin/env python3
# madLib.py - Replaces ADJECTIVE, NOUN, ADVERB, VERB with user input

import re, os, sys
def usage():
    print('Usage: madLib.py <file_name>')

madLibRegex = re.compile(r'(ADJECTIVE|NOUN|ADVERB|VERB)')


