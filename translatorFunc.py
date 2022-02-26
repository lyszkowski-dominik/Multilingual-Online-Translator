import requests

headers = {'User-Agent': 'Mozilla/5.0'}


def getPage(translation, word):
    address = 'https://context.reverso.net/translation/{}/{}'.format(translation, word)
    r = requests.get(address, headers=headers)
    if r.status_code == 200:
        return r
    else:
        print("Error while getting data")


def displayMenu():
    languages = ['', 'arabic', 'german', 'english', 'spanish', 'french', 'hebrew', 'japanese', 'dutch', 'polish',
                 'portuguese', 'romanian', 'russian', 'turkish']
    print("Hello, you're welcome to the translator. Translator supports: ")
    for i in range(1, 14):
        print(str(i) + ". " + languages[i].capitalize())
    a = languages[int(input("Type the number of your language:"))]
    b = languages[int(input("Type the number of language you want to translate to:"))]
    word = input("Type the word you want to translate:")
    direction = a + '-' + b
    fromTo = [direction, word, b]
    return fromTo


def filterWords(site):
    words = []
    sentencesFrom = []
    sentencesTo = []
    # filter translated words
    for para in site.find_all(class_='translation'):
        words.append(para.get_text().strip())
    words.remove("Translation")
    # filter translated sentence native
    for para in site.find_all('div', 'src ltr'):
        sentencesFrom.append(para.get_text().strip())
    # filter translated sentence target
    for para in site.find_all('div', 'trg ltr'):
        sentencesTo.append(para.get_text().strip())
    extractedData = [words, sentencesFrom, sentencesTo]
    return extractedData


def presentData(data, choices):
    print("{} Translations:".format(choices[2].capitalize()))
    # print only 5 translated words
    for i in range(5):
        print(data[0][i])
    print("\n")
    print("{} Examples:".format(choices[2].capitalize()))
    # print 5 translated sentences native / target
    for i in range(5):
        print(data[1][i])
        print(data[2][i])
        print("\n")
