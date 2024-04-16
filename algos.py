import requests
from random import randint
import time
from config import *
from qr_code import *

def attaque (x : list, y : list, couleur : str, url : str, params : set, headers : set) -> None :
    map = genmap(map_arr)
    attaquer = []
    for i in range(x[0], x[1]+1):
        for j in range(y[0], y[1]+1):
            pos = f'{i},{j}'
            if couleur != map[pos]:
                attaquer.append(f'{i},{j}')

    while len(attaquer) > 0:

        for id in ids:

            pos = attaquer.pop(randint(0,len(attaquer)-1))
            data = f'42["update","{pos}","{couleur}","{id}"]'

            response = requests.post(url, headers=headers, params=params, data=data)
            print(response.status_code)
            print(response.text)

            if len(attaquer) == 0 : 
                print("Attaque terminée.")
                exit()

        print('Tour terminé, attende de 50s...')
        time.sleep(50)

def qr_attaque (x : list, y : list, data : str, url : str, params : set, headers : set) -> None:
    map = genmap(map_arr)
    qr_noir = gen_QR(data)
    qr_noir_fix = []
    for i in qr_noir :
        x_fix, y_fix = i.split(",")
        x_fix = str(int(x_fix)+x[0])
        y_fix = str(int(y_fix)+y[0])
        if map[f'{x_fix},{y_fix}'] != "black" :
            qr_noir_fix.append(f'{x_fix},{y_fix}')
    # blanc
    qr_blanc = []
    for i in range(x[0], x[1]+1):
        for j in range(y[0], y[1]+1):
            pos = f'{i},{j}'
            if map[pos] != "white" :
                qr_blanc.append(f'{i},{j}')
    
    while len(qr_blanc) > 0 or len(qr_noir_fix) > 0 :

        for id in ids:

            if len(qr_blanc)>0 :
                pos = qr_blanc.pop(randint(0,len(qr_blanc)-1))
                data = f'42["update","{pos}","white","{id}"]'

                response = requests.post(url, headers=headers, params=params, data=data)
                print(response.status_code)
                print(response.text)

                if len(qr_blanc) == 0 : 
                    print("Cases blanches placées.")

                continue
            
            elif len(qr_noir_fix)>0 :
                pos = qr_noir_fix.pop(randint(0,len(qr_noir_fix)-1))
                data = f'42["update","{pos}","black","{id}"]'

                response = requests.post(url, headers=headers, params=params, data=data)
                print(response.status_code)
                print(response.text)

                if len(qr_noir_fix) == 0 : 
                    print("Cases noires placées.")
                    break

        print('Tour terminé, attende de 50s...')
        time.sleep(50)
    
    print("QR code complété.")