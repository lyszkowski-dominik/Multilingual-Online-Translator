import requests

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


def displayMenu():
    print("Hello, you're welcome to the translator. Translator supports: ")
    print(
        "1. Arabic\n2. German\n3. English\n4. Spanish\n5. French\n6. Hebrew\n7. Japanese\n8. Dutch\n9. Polish\n10. Portuguese\n11. Romanian\n12. Russian\n13. Turkish")
    a = input("Type the number of your language:")
    b = input("Type the number of language you want to translate to:")
    word = input("Type the word you want to translate:")
    fromTo = [a, b, word]
    return fromTo
