import webbrowser
import sys
import pyperclip
import requests

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

address = address.replace(' ', '%20')
#webbrowser.open("https://www.google.com/maps/place/" + address)

print(address)

# https://automatetheboringstuff.com/files/rj.txt

res = requests.get("https://automatetheboringstuff.com/files/rj.txt")

text_file = open('text.txt', 'w')
text_file.write(res.text)

print(res.text[0])
