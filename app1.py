from selenium import webdriver
import webbrowser
import sys
import pyperclip
import requests
import bs4
'''
You enter your keyword, and automatically the code opens the first 5 of its google search.
'''


arr = []
keyword = ''
if len(sys.argv) > 1:
    arr = sys.argv[1:]
    for arg in arr:
        keyword += arg + '+'
        print(arg)
else:
    keyword = ''
    print('There is no keyword to search for add keywords to your argument')

url = 'http://google.com/search?client=safari&rls=en&q=' + keyword
text = requests.get(url)
Soup_Var = bs4.BeautifulSoup(text.text, 'html.parser')
All_Links = Soup_Var.select('.kCrYT a')
numOpen = min(5, len(All_Links))
for i in range(numOpen):
    webbrowser.open('http://google.com' + All_Links[i].get('href'))
