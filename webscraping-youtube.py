import requests
from bs4 import BeautifulSoup
import webbrowser

def vids_list(search):
    url = 'https://www.youtube.com/results?search_query=' + search
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    a = soup.find_all("a", {'class': "yt-uix-tile-link"})
    vid_dict = {}
    for i in a:  # run the a list
        if len(vid_dict) > 6:
            break
        else:
            vid_name = i['title']
            watch_link = i['href']
            final_link = 'https://www.youtube.com/' + watch_link
            vid_dict[vid_name] = final_link
        
    return vid_dict

search = input('Digite o nome da música: ').strip().replace(' ', '+')
videos = vids_list(search)
titles = []  # Lista para armazenar os títulos ordenadamente

for c,key in zip(range(len(videos)),videos.keys()): # Guarda os títulos na lista e printa em ordem
    titles.append(key)
    print(f'{c+1} - {key}')
op = int(input('Qual video deseja abrir? '))
final_url = videos[titles[op-1]]
webbrowser.open_new_tab(final_url)
