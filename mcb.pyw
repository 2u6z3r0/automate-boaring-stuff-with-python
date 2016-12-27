# chapter 8 - practice 2, Multiclipboard
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys


def usage():
    print('''Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
             py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
             py.exe mcb.pyw list - Loads all keywords to clipboard.
           ''')

mcbShelf = shelve.open('mcb')
# save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
# list keyword
elif sys.argv[1] == 'list':
    pyperclip.copy(str(list(mcbShelf.keys())))
# copy content to clipboard
elif sys.argv[1] in mcbShelf:
    pyperclip.copy(mcbShelf[sys.argv[1]])

else:
    usage()

mcbShelf.close()
