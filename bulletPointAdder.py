#/usr/bin/env python3
#It adds a bullet point for every new line to copied text
#first copy the text to clipboard, which need bullet to be added in evevy line
#After copying run this scirpt, and paste the new text with bullet added

import pyperclip

text = pyperclip.paste()
lines = text.split('\n')
for i in range(len(lines)):     #loop through all indexes
    lines[i] = '*' + lines[i]   #add * infront of each new line

newText = '\n'.join(lines)
pyperclip.copy(newText)
print('added bullet point infront of every new line, paste it to see')
