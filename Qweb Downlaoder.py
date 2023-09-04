import requests
from bs4 import BeautifulSoup

url = 'https://musicguitars.ir/page/2/'
artistNames = ['ابی', 'اندی', 'شهره', 'گوگوش', 'مارتیک']

try:
    response = requests.get(url)

    if response.status_code == 200:
        mainContent = BeautifulSoup(response.text, 'html.parser')
        posterts = mainContent.find_all('article', class_='gmmpost')

        for post in posterts:
            h2Tag = post.find("h2", class_="gmmah")
            if h2Tag:
                aTag = h2Tag.find('a', href=True)
                if aTag:
                    aTagLink = aTag['href']
                    aText = aTag.text.strip()

                    if any(name in aText for name in artistNames):
                        print(f'Founded : {aText}')

                        response_article = requests.get(aTagLink)

                        if response_article.status_code == 200:
                            mainContent_article = BeautifulSoup(
                                response_article.text, 'html.parser')
                            dlContainer = mainContent_article.find(
                                "div", class_="gmdllink gmfx")

                            if dlContainer:
                                dlLink = dlContainer.find_all('a', class_='dl', href=True)
                                for dl in dlLink:
                                    dlLinkHref = dl['href']
                                    if dlLinkHref.endswith('[320].mp3'):
                                        print(dlLinkHref)


                                
                            else:
                                print('Download container not found.')
                        else:
                            print(
                                f'Error opening article link: {response_article.status_code}')
            else:
                print('Nothing Found :)')
                backup = open('q.txt', 'w')
                backup.write(str(mainContent))
    else:
        print(f'Error : {response.status_code}')

except requests.exceptions.RequestException as e:
    print(f'Could not Connect: {str(e)}')
