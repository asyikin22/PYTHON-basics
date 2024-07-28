print("testing")
import pyperclip

#copy text to the clipboard
pyperclip.copy("Hello, Asyikin")

#retrieve text from clipboard
greeting = pyperclip.paste()

#print the retrieved text
print("Text from clipboard: ", greeting, "\n")

# Multi-Clipboard Automatic Messages
print('Multi-Clipboard Automatic Messages')
import sys
import pyperclip

TEXT = {
    'Setuju': '''Ya, saya setuju.''',
    'Sibuk': '''Maaf, saya tidak ada kelapangan minggu ini.''',
    'Townhall': '''Town hall akan berjalan seperti biasa Isnin ini.'''}

if len(sys.argv) < 2:
    print('Usage: py 3-strings.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]    #first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print("Text for " + keyphrase + ' copied to clipboard.')

    mesej = TEXT[keyphrase]
    print("Mesej dari keyphrase 'setuju': " + mesej)

else:
    print('These is no text for ' + keyphrase)

