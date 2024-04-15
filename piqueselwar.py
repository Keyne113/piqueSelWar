from algos import *

url = 'https://pixelwar.insash.fr/socket.io/'
params = {
    'transport': 'polling',
    'sid': 'DdUM7b6WXrdyx5tgAFlq'       # a modif a chaque fois
}

headers = {
    'Host': 'pixelwar.insash.fr',
}

# ATTAQUE

couleur = "white"
x = [94,118]
y = [94,118]

# QR CODE

qr_attaque([90,119], [90,119], "https://www.youtube.com/watch?v=LwEq6fHP5SA")  # pop simokééé