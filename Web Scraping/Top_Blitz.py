# importar librerias
import re
import requests #peticion al servidor
import lxml.html as html
import pandas as pd
from bs4 import BeautifulSoup


website = 'https://www.chess.com/ratings'
rq = requests.get(website)
soup = BeautifulSoup(rq.text,'html.parser')

# Players
players_chess = soup.find_all('a', class_="master-players-rating-username")
players_name =list()

count = 0

for i in players_chess:
    if count < 10:
        players_name.append(i.text)
    else:
        break
    count += 1


# Elo
players_points = soup.find_all('div', class_="master-players-rating-player-rank")
players_elo =list()

count = 0

for i in players_points:
    if count < 10:
        players_elo.append(i.text)
    else:
        break
    count += 1


# Ranking
players_rank = soup.find_all('div', class_="master-players-rating-rank")
players_rat =list()

count = 0

for i in players_rank:
    if count < 10:
        players_rat.append(i.text)
    else:
        break
    count += 1


df = pd.DataFrame({'Name':players_name, 'Elo':players_elo, 'Rank':players_rat}, index=list(range(1,10)))

