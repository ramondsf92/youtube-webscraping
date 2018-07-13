import requests
from bs4 import BeautifulSoup
import webbrowser

def vids_list(search):
    url = ''
    ytlink = 'https://www.youtube.com'
    url = 'https://www.youtube.com/results?search_query=' + search
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    a = soup.find_all('a') # links for videos are 'a'
    vid_dict = {}
    for i in a: # run the a list
        if len(vid_dict) > 4:
            break
        else:
            n = i.get('class') # get the class of all a
            if n == ['yt-uix-tile-link', 'yt-ui-ellipsis', 'yt-ui-ellipsis-2', 'yt-uix-sessionlink', 'spf-link', '']:
                '''
                here we locate all classes that are common between the links for the videos, and I'm taking the href from 
                everyone. I did it just inspecting the webpage and location the <a> section by passing the mouse pointer
                above the links.
                '''
                vid_name = i.get('title')
                watch_link = i.get('href')
                final_link = ytlink + watch_link
                vid_dict[vid_name] = final_link
    return vid_dict

search = input('Digite o nome da música: ').strip().replace(' ','+')
videos = vids_list(search)
titles = [] # Lista para armazenar os títulos ordenadamente
for c,key in zip(range(len(videos)),videos.keys()): # Guarda os títulos na lista e printa em ordem
    titles.append(key)
    print(f'{c+1} - {key}')
op = int(input('Qual video deseja abrir? '))
final_url = videos[titles[op-1]]
webbrowser.open_new_tab(final_url)