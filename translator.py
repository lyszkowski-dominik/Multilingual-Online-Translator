import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0'}


def getPage(translation, word):
    address = 'https://context.reverso.net/translation/{}/{}'.format(translation, word)
    print(address)
    r = requests.get(address, headers=headers)
    if r.status_code == 200:
        print(str(r.status_code) + " OK")
        return r
    else:
        print("Error while getting data")


translationWay = {'en': 'french-english', 'fr': 'english-french'}
languages = {'en': 'English', 'fr': 'French'}
words = []
sentences1 = []
sentences2 = []
language = input('Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:')
word = input("Type the word you want to translate:")
print('You chose "{}" as a language to translate "{}" to'.format(language, word))

translation = translationWay[language]
r = getPage(translation, word)
soup = BeautifulSoup(r.content, 'html.parser')
for para in soup.find_all(class_='translation'):
    words.append(para.get_text().strip())
words.remove("Translation")
print("{} Translations:".format(languages[language]))
print(*words[0:5], sep="\n")
for para in soup.find_all('div', 'src ltr'):
    sentences1.append(para.get_text().strip())
for para in soup.find_all('div', 'trg ltr'):
    sentences2.append(para.get_text().strip())

print("\n")
print("{} Examples:".format(languages[language]))
for i in range(5):
    print(sentences1[i])
    print(sentences2[i])
    print("\n")

