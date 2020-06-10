# youtube-webscraping

Web Scraping com Python para pesquisa de vídeos no youtube.

Usadas as bibliotecas requests e BeautifulSoup para raspagem web, mais webbrowser para abrir a url no navegador.
A principio a ideia era fazer um music bot para o Discord, porém aprendi apenas a colocar a música pra tocar mandando
a url do vídeo pelo Discord. Pensando em otimizar o processo, busquei retornar a url através apenas da palavra-chave,
usando o sistema de busca do YouTube. Por enquanto esse é o projeto, que através da palavra-chave, me mostra os 5 primeiros
vídeos que aparecem na página do YT e seleciona um deles através de um input.

Na prática, após rodar o script, insere-se o nome do vídeo a ser pesquisado (como se estivesse inserindo na barra de pesquisa do youtube)
e ele retorna uma lista com as opções. Então deve ser inserido o número referente ao vídeo desejado. Após isso, o navegador será aberto automaticamente com a página do video já carregada.
