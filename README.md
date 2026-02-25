
# zadanie-rekrutacyjne-solar-plane-socket
Prosty system do odbierania danych z drona.
Dron (klient) wysyła zdjęcie i komunikat, a serwer (stacja naziemna) pokazuje to na stronie WWW, z uzyciem websockets

## Jak to działa?

1. **Dron (skrypt `dron_klient.py`):**
   * Bierze zdjęcia z folderu `zdjecia_z_drona`.
   * Wysyła je co 10 sekund na serwer za pomocą zwykłego żądania HTTP POST.
   * Dorzuca do każdego zdjęcia krótki tekst związany z nazwa zdjęcia.

2. **Serwer (skrypt `stacja_serwer.py`):**
   * Odbiera pliki i zapisuje je w folderze `static/uploads`.
   * Wystawia stronę internetową, która wyświetla ostatnie odebrane zdjęcie i tekst za pomoca socketio.
   * zdjecie i jego opis sa wysylane na strone za pomoca biblioteki socketio, dzieki czemu zdjecia po wyslaniu z 'drona' wyswietlaja sie od razu na stronie 
## Jak to uruchomić

`pip install flask requests flask-socketio`
w pliku `dron_klient.py` jest adres localhost `http://127.0.0.1:5000` przez co program działa lokalnie na urządzeniu na kotrym jest odpalony,
ale jesli zmieni sie to na `http://(adres IP):5000` i pominie zapore sieci to bedzie działał na urządzeniach podpiętych do tej samej sieci.
najpierw nalezy odpalić python stacja_serwer.py potem otworzyc strone, potem odpalic python dron_klient.py. i patrzec na zmieniające się zdjęcia:) 
