import qrcode
import numpy as np
from PIL import Image

def gen_QR(data : str) -> list:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=1,
        border=1
    )
    qr.add_data(data)
    qr.make(fit=True)


    img = qr.make_image(fill_color="black", back_color="white").convert('1')

    array = np.array(img)

    qr_noir = []
    for y in range(array.shape[0]):
        for x in range(array.shape[1]):
            if array[y, x] == 0:
                qr_noir.append(f"{x},{y}")

    return qr_noir