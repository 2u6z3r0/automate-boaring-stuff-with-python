# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

def usage():
    print('mscb')
# TODO: save clipboard content
if len(sys.argv) == 3:
    if sys.argv[1] == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.copy()
# TODO: list keyword and load content

mcbShelf.close()