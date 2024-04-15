from algos import *

url = 'https://pixelwar.insash.fr/socket.io/'
params = {
    'transport': 'polling',
    'sid': 'DdUM7b6WXrdyx5tgAFlq'       # a modif a chaque fois
}

headers = {
    'Host': 'pixelwar.insash.fr',
}

couleur = "white"
x = [90,119]
y = [90,119]
data = "https://www.youtube.com/watch?v=LwEq6fHP5SA"


# attaque(x, y, couleur, url, params, headers)

qr_attaque(x, y, data, url, params, headers)  # pop simokééé