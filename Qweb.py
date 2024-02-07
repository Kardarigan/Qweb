import requests
import datetime
from bs4 import BeautifulSoup


print("""
\033[93m                    ,&OO#O$,             
                 OOO.     (OOO        
                OO           (OO      
                OO       OOOO   OO-----O
    OOO          OO              OO ...O
  .OO   OOO      OO,            OO____O 
 &OO       OO%OOOOOOO          OO       
 OO                           OO      
#O                             OO   \033[30m'Hello there, World'
\033[93m%O            ________        (O%   \033[36m-> GitHub : \033[31mhttps://github.com/Kardarigan
\033[93mOO           |                 OO   \033[36m-> Website : \033[31mhttp://qmars.gigfa.com/
\033[93mOO,           |________        OO      
  OO                         (OO       
    OOOOO                  %OO
        .OOOOOOOOOOOOOOOO*
""")


while True:
    finalDestination = input('\033[94mEnter Destination Index : ')
    finalDestination = int(finalDestination)
    finalDestination += 1
    nowTime = datetime.datetime.now()
    nowTime = nowTime.strftime('%Y%m%d%H%M')
    nowFileName = ''.join(filter(str.isdigit, nowTime))
    with open('allLinks.txt', 'w') as backup:
        pass

    for pageIntex in range(1, finalDestination):
        url = f'https://musicgtars.ir/page/{pageIntex}/'
        artistNames = [' ابی ', ' اندی ', ' شهره ', 'گوگوش', 'مارتیک']
        forbiddens = ['ریمیکس','فول','هوش مصنوعی','گلچین']

        try:
            response = requests.get(url)
            if response.status_code == 200:
                mainContent = BeautifulSoup(response.text, 'html.parser')
                posterts = mainContent.find_all('article', class_='gmmpost')
                for post in posterts:
                    h2Tag = post.find('h2', class_='gmmah')
                    if h2Tag:
                        aTag = h2Tag.find('a', href=True)
                        aTagLink = aTag['href']
                        aText = aTag.text.strip()
                        if any(name in aText for name in artistNames):
                            if any(name in aText for name in forbiddens):
                                print('\033[31mIts Forbiden')
                            else: 
                                pass
                            print(f'\033[32mFounded :\033[35m {aText} ---- Page : {pageIntex}')
                            response_article = requests.get(aTagLink)
                            if response_article.status_code == 200:
                                mainContent_article = BeautifulSoup(response_article.text, 'html.parser')
                                dlContainer = mainContent_article.find('div', class_='gmdllink gmfx')
                                dlContainerAlbum = mainContent_article.find('div', class_='gmmpostc')

                                if dlContainer:
                                    dlLink = dlContainer.find_all(
                                        'a', class_='dl', href=True)
                                    for dl in dlLink:
                                        dlLinkHref = dl['href']
                                        if dlLinkHref.endswith('[320].mp3'):
                                            print(dlLinkHref)
                                            with open(f'Qweb-{nowFileName}.txt', 'a') as backup:
                                                backup.write(f'{dlLinkHref}\n')
                                elif dlContainerAlbum:
                                    dlLink = dlContainerAlbum.find_all(
                                        'a', class_='gmsdl', href=True)
                                    for dl in dlLink:
                                        dlLinkHref = dl['href']
                                        if dlLinkHref.endswith('[320].mp3'):
                                            print(dlLinkHref)
                                            with open(f'Qweb-{nowFileName}.txt', 'a') as backup:
                                                backup.write(f'{dlLinkHref}\n')
                                else:
                                    print('Download container not found.')
                            else:
                                print(
                                    f'Error opening article link: {response_article.status_code}')
                    else:
                        print('Nothing Found :)')
            else:
                print(f'Error : {response.status_code}')
        except requests.exceptions.RequestException as e:
            print(f'Could not Connect: {str(e)}')
    input("\033[94mPress 'Enter' Key to Restart...")
