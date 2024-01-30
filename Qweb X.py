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

    for pageIntex in range(1, finalDestination):
        url = f'https://musicguitars.ir/page/{pageIntex}/'
        artistNames = ['25باند', '2AFM', '2PAC', 'B.I.G', 'Billie Eilish', 'Camila Cabello', 'DEMIS ROUSSOS', 'EMINEM', 'Enrique', 'Jolio iglesias', 'Kendrick Lamar', 'MARIAH CAREY', 'MICHAEL JACKSON', 'MODERN TALKING', 'Shagy', 'Tatu', 'TMBAX', 'آرش', 'آرش و مسیح', 'آقاسی', 'ابی', 'احسان خواجه امیری', 'احمدآزاد', 'ادو', 'ادی عطار', 'اسی', 'اشوان', 'افتخاری', 'افشین', 'افشین مقدم', 'افو', 'السید', 'امید', 'امید جهان', 'امید حاجیلی', 'امیر خلوت', 'امیرتاجیک', 'امیرعباس گلاب', 'امین بانی', 'اندی', 'اوا', 'ایرج خواجه امیری', 'ایرج مهدیان', 'ایشان', 'اینه', 'ایوان باند', 'بابک امینی', 'بابک جهانبخش', 'باران', 'بتی', 'بروانه', 'بروبکس', 'بلاک کتس', 'بنان', 'بنیامین', 'بهرام حصیری', 'بهرام رادان', 'بهنام بانی', 'بیژن خاوری', 'بیژن مرتضوی', 'تتلو', 'تهی', 'تیک تاک', 'جاستینا', 'George Michael', 'جلال همتیان', 'جمال وفایی', 'جمشید', 'جهان', 'جوادمعروفی', 'جوادیساری', 'حامدنیک بی', 'حامدهمایون', 'حامی', 'حبیب', 'حجت اشرف زاده', 'حسین زمان', 'حمیدخندان', 'حمیدطالب زاده', 'حمیدعسکری', 'حمیدغلامعلی', 'حمیدهیراد', 'حمیرا', 'خلسه', 'داریوش', 'داوود بهبودی', 'داوودمقامی', 'دریادادور', 'دلارام', 'رامش', 'رستاک', 'رضا پیشرو', 'رضا یزدانی', 'رضاصادقی', 'رهااعتمادی', 'روح پرور', 'روزبه بمانی', 'روزبه نعمت الهی', 'ریکادو', 'زانیار', 'زخمی و سوگند', 'زدبازی', 'ساسی', 'سالارعقیلی', 'سامان', 'سامی بیگی', 'سانبوی', 'ستار', 'سحر', 'سروش', 'سرژیک', 'سعید', 'سعید شایسته', 'سعیدشهروز', 'سعیدمحمدی', 'سلی', 'سندی', 'سوزان روشن', 'سپهر', 'سپیده', 'سیاوش قمیشی', 'سیاوُش شمس', 'سیروان خسروی', 'سیلوئیت', 'سیمین غانم', 'سیناسرلک', 'شادمهر عقیلی', 'شاهرخ', 'شاهکاربینش پژو', 'شایع', 'شراره', 'شماعی زاده', 'شهاب', 'شهاب تیام', 'شهاب مظفری', 'شهرام شب پره', 'شهرام شکوهی', 'شهرام صولتی', 'شهرام ناظری', 'شهرام کاشانی', 'شهره', 'شهریار', 'شهلا سرشار', 'شهیاد', 'شکیلا', 'شیلا', 'صادق نوجوکی', 'ضیاء', 'طوفان', 'عارف', 'عباس قادری', 'عرفان', 'علی دانیال', 'علی زند وکیلی', 'علی ظلیسچی', 'علی عبدالمالکی', 'علی لهراسبی', 'علی نظری', 'علیرضاعصار', 'علیرضاقربانی', 'عمادرام', 'عمادطالبزاده', 'عمادقویدل', 'عهدیه', 'غلامرضاصنعتگر', 'فتانه', 'فرامرز آصف', 'فرامرز اصلانی', 'فرامرز محجوب', 'فرزاد فرزین', 'فرزین', 'فرشته', 'فرشیدامین', 'فرهادبزله', 'فرهادجواهرکلام', 'فرهادمهراد', 'فریدون آسرایی', 'فریدون فرخزاد', 'فریدون فروغی', 'قاسم افشار', 'قیصر', 'لیلافروهر', 'مارتیک', 'مازیار', 'مازیارعصری', 'مازیارفلاحی', 'مانی رهنما', 'ماه بانو', 'ماکان باند', 'مجیداخشابی', 'محسن چاوشی', 'محسن یگانه', 'محمداصفهانی', 'محمدرضاگلزار', 'محمدعلیزاده', 'محمدنوری', 'محمودقربانی', 'مرتضی', 'مرتضی پاشایی', 'مرجان', 'مریم جلالی', 'مسعودصادقلو', 'معراج محمدی', 'معین', 'منصور', 'مهدی مقدم', 'مهدی یراحی', 'مهران مدیری', 'مهردادآسمانی', 'مهردادکاظمی', 'مهرشاد', 'مهساناوی', 'مهستی', 'مونتیگو', 'مکابیز', 'میثم ابراهیمی', 'نازی افشار', 'ناصرعبدالهی', 'ناصرمسعودی', 'ناصرچشم آذر', 'ناهید', 'نلی', 'نوش آفرین', 'نیما', 'هاتف', 'هایده', 'هفت گروه', 'هلن', 'همایون شجریان', 'هنگامه', 'هوشمندعقیلی', 'هیچکس', 'وفا', 'ویگن', 'پارسالیپ', 'پازل باند', 'پری زنگنه', 'پویا', 'پیروز', 'چنگیز حبیبیان', 'ژاکلین', 'کامران هومن', 'کاوه یغمایی', 'کمپانی خط', 'کوروس', 'کوروش یغمائی', 'گامنو', 'گرشارضائی', 'گروه آرین', 'گروه رستاک', 'گروه سون', 'گلشیفته فراهانی', 'گلپایگانی', 'گوگوش', 'گیتا', 'گیتی', 'یاس', 'Dua Lipa', 'Sandra', 'Laura Branigan', 'Chris de Burgh', 'بویز', 'Lionel Richie', 'Beatles', 'Kenny G', 'هیپ هاپولوژیست', 'Ghost', 'حسن شجاعی']
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
                                print('\033[31mIts Forbidden')
                            else:
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