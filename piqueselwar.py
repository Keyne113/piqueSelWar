import requests
from random import randint
import time
from config import ids

url = 'https://pixelwar.insash.fr/socket.io/'
params = {
    'transport': 'polling',
    'sid': 'qZX1y4WJ_XC_tfgiADxI'       # a modif a chaque fois
}

headers = {
    'Host': 'pixelwar.insash.fr',
}

# ATTAQUE

couleur = "white"
x = [95, 112]
y = [70, 87]
attaquer = []
for i in range(x[0], x[1]+1):
    for j in range(y[0], y[1]+1):
        attaquer.append(f'{i},{j}')

while True:

    for id in ids:
        data = f'42["update","{attaquer.pop(randint(0,len(attaquer)-1))}","{couleur}","{id}"]'

        response = requests.post(url, headers=headers, params=params, data=data)

        print(response.status_code)
        print(response.text)

    print('Tour terminé, attende de 50s...')
    time.sleep(50)