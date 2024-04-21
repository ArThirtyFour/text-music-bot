import json
import requests
from bs4 import BeautifulSoup
from config import api_token
def clear_html(url_1,text):
    text = text.replace('<br/>','\n').replace('<div class="Lyrics__Container-sc-1ynbvzw-1 kUgSbL" data-lyrics-container="true">','').replace('</div>','')
    listur_delete = ['<span class="ReferentFragmentdesktop__Highlight-sc-110r0d9-1 jAzSMw>',
    '<span class="ReferentFragmentdesktop__Highlight-sc-110r0d9-1 jAzSMw>','</a>','<a>','</span>','<span>', '</i>','<i>',
    '<span style="position:absolute;opacity:0;width:0;height:0;pointer-events:none;z-index:-1" tabindex="0">','<span class="ReferentFragmentdesktop__Highlight-sc-110r0d9-1 jAzSMw">',
    '<a class="ReferentFragmentdesktop__ClickTarget-sc-110r0d9-0 cesxpW"', 'href=',f'/{url_1}/">','&amp;']
    for i in listur_delete:
        text = text.replace(i,'')
    return text
def get_url_song (text):
    headers = {"Authorization": f"Bearer _{api_token}"}
    text = text.lower().replace(' ','%20')
    q = requests.get(f'https://api.genius.com/search?q={text}',headers=headers).text
    data_dict = json.loads(f'{q}')
    try:
        return data_dict['response']['hits'][0]['result']['url']
    except:
        return 'Не удалось достать!'
def get_text(name , url):
    if url =='Не удалось достать!':
        return False
    else:
        url_1 = url.split('/')[-1].replace('-lyrics','')
        print(url_1)
        q = requests.get(url)
        bs = BeautifulSoup(q.text,'html.parser')
        all_lyrics = bs.find_all('div',class_='Lyrics__Container-sc-1ynbvzw-1 kUgSbL')
        with open(f'{name}.txt','w+',encoding='utf-8') as file:
            for i in all_lyrics:
                text = i.prettify()
                file.write(clear_html(url_1,text))
        return True
