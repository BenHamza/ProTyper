import urllib as ac
from bs4 import BeautifulSoup

import html5lib


import urllib
r = ac.urlopen('http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts').read()
#r = urllib.urlopen('http://10fastfingers.com/typing-test/german').read()
#a = html5lib.parse(r )
soup = BeautifulSoup(r, 'html5lib')

letters = soup.find_all("div", class_="ec_statements")




lobbying = {}
for element in letters:
    lobbying[element.a.get_text()] = {}

print letters[0].a["href"]