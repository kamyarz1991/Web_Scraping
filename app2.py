from selenium import webdriver
import webbrowser
import sys
import pyperclip
import requests
import bs4


'''
----
Download pages with the requests module.

Find the URL of the comic image for a page using Beautiful Soup.

Download and save the comic image to the hard drive with iter_content().

Find the URL of the Previous Comic link, and repeat.

'''


url = 'https://xkcd.com/'
href = '//'
i = 1

while href.strip('/') != "1":

    request = requests.get(url+href)
    Beu_Soup = bs4.BeautifulSoup(request.text, 'html.parser')
    Img_Soup = Beu_Soup.select('#comic img')
    Prev_Soup = Beu_Soup.select(
        'ul.comicNav:nth-child(2) > li:nth-child(2) > a:nth-child(1)')
    href = Prev_Soup[0].get('href')
    print(len(Img_Soup))
    try:
        Image_URL = 'https:' + Img_Soup[0].get('src')
    except IndexError:
        continue
    print(href)
    try:
        response = requests.get(Image_URL, stream=True)
    except requests.exceptions.RequestException as e:
        print(e)
        continue
    imageFile = open('pic_' + str(i) + '.jpg', 'wb')
    for block in response.iter_content(1024):

        imageFile.write(block)
    imageFile.close()

    i += 1
