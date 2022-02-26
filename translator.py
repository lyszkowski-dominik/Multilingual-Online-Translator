from bs4 import BeautifulSoup
from translatorFunc import getPage


translationWay = {'en': 'french-english', 'fr': 'english-french'}
languages = {'en': 'English', 'fr': 'French'}
words = []
sentences1 = []
sentences2 = []
language = input('Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:')
word = input("Type the word you want to translate:")
print('You chose "{}" as a language to translate "{}" to'.format(language, word))

translation = translationWay[language]
# get translation page
r = getPage(translation, word)
soup = BeautifulSoup(r.content, 'html.parser')
# filter translated words
for para in soup.find_all(class_='translation'):
    words.append(para.get_text().strip())
words.remove("Translation")
print("{} Translations:".format(languages[language]))
# print only 5 translated words
print(*words[0:5], sep="\n")
# filter translated sentence native
for para in soup.find_all('div', 'src ltr'):
    sentences1.append(para.get_text().strip())
# filter translated sentence target
for para in soup.find_all('div', 'trg ltr'):
    sentences2.append(para.get_text().strip())

print("\n")
print("{} Examples:".format(languages[language]))
# print 5 translated sentences native / target
for i in range(5):
    print(sentences1[i])
    print(sentences2[i])
    print("\n")

