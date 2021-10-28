produkty = {"marchew":"2.34", "pietruszka":"2.34"}
cenafdf = dict(tak=3.45,mar=675.4)
zamowiene = {}

print("Siemka w żabencji mamy: ")
for pr in produkty.keys():
    print(" - ",pr," w cenie ", produkty.get(pr), " za kg")

staff = False
haslo = input("Jak jesteś klient to kliknij enter a jak kasjer to dej no hasło na kajzerke:")
if haslo == "1234":
    staff = True

while staff==False:
    while 1:
        produkt = input("Co chcesz kupić?")
        if produkt in produkty.keys():
            kg = input("Ile mordo?")
            zamowiene.setdefault(produkt, 0)
            zamowiene[produkt] += int(kg)
            pyt = input("Chcesz cos jeszcze? TAK/NIE")
            if pyt == "TAK":
                continue
            else:
                break
        else:
            print("Nie mamy tego byczqu :(")
    suma = 0
    for zam_co, zam_ile in zamowiene.items():
        ile = float(zam_ile)
        cena = float(produkty['marchew'])
        suma = ile * cena
    print("Elo dej ", suma)
while staff == True:
    break

