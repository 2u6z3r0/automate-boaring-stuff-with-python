# chapter 8 - practice 2, Multiclipboard
# Usage: python3 mcbExtended.pyw save <keyword> - Saves clipboard to keyword.
# python3 mcbExtended.pyw <keyword> - Loads keyword to clipboard.
# python3 mcbExtended.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys


def usage():
    print('''Usage: python3 mcbExtended.pyw save <keyword> - Saves clipboard to keyword.
             python3 mcbExtended.pyw <keyword> - Loads keyword to clipboard.
             python3 mcbExtended.pyw list - Loads all keywords to clipboard.
           ''')

mcbExtendedShelf = shelve.open('mcbExtended')
# save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbExtendedShelf[sys.argv[2]] = pyperclip.paste()

# delete keyword
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbExtendedShelf[sys.argv[2]]

elif len(sys.argv) == 2:
    # list keyword
    if sys.argv[1] == 'list':
        pyperclip.copy(str(list(mcbExtendedShelf.keys())))

    # copy content to clipboard
    elif sys.argv[1] in mcbExtendedShelf:
        pyperclip.copy(mcbExtendedShelf[sys.argv[1]])

    # delete all keywords i.e clear the shelve
    elif sys.argv[1] == 'delete':
        mcbExtendedShelf.clear()

    # print usage
    else:
        usage()

# print usage
else:
    usage()

mcbExtendedShelf.close()
