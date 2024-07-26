#Multi-Clipboard Automatic Messages
print('Multi-clipboard Automatic Messages')
import pyperclip

#copy text to the clipboard
pyperclip.copy("Hello, Asyikin")

#retrieve text from clipboard
greeting = pyperclip.paste()

#print the retrieved text
print("Text from clipboard: ", greeting)