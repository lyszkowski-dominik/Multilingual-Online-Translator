from bs4 import BeautifulSoup
from translatorFunc import getPage, displayMenu, filterWords, presentData


translationWay = {'en': 'french-english', 'fr': 'english-french'}
languages = {'en': 'English', 'fr': 'French'}


choices = displayMenu()

# Get page with translation
r = getPage(choices[0], choices[1])
site = BeautifulSoup(r.content, 'html.parser')

output = filterWords(site)
presentData(output, choices)
