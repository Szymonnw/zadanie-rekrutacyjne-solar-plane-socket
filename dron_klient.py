import os
import time
import requests


sciezka_folderu = 'zdjecia_z_drona'
URL = 'http://127.0.0.1:5000/upload'

for plik in os.listdir(sciezka_folderu):
    with open(os.path.join(sciezka_folderu, plik), 'rb') as zdjecie:
        paczka_pliki = {'zdjecie': zdjecie}
        paczka_tekst = {'tekst': f"taka jest nazwa {plik}"}
        odp = requests.post(URL, files=paczka_pliki, data=paczka_tekst)
        print(f"Status: {odp.status_code} , {odp.text}")
    time.sleep(10)




