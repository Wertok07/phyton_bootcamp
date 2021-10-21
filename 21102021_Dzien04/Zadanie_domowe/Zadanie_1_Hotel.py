"""
Program wyliczający opłatę za pobyt w hotelu
"""

wiek = 0
liczba_nocy = 0
oplata = 0

def oplata_dorosli(noce):
    if noce == 1:
        op = 200
    elif noce >= 5:
        op = 150*noce
    else:
        op = 180*noce
    return op

print("Witaj w hotelu MARMUR")

wiek = int(input("Podaj swój wiek: "))
liczba_nocy = int(input("Podaj liczbę nocy: "))

if wiek < 18:
    oplata = liczba_nocy*100
    print(f"Witaj nieletni, Twoja opłata za {liczba_nocy} nocy wynosi: {oplata:.2f}zł")
elif wiek >= 18 and wiek <65:
    oplata = oplata_dorosli(liczba_nocy)
    print(f"Witaj dorosły, Twoja opłata za {liczba_nocy} nocy wynosi: {oplata:.2f}zł")
else:
    oplata = oplata_dorosli(liczba_nocy)*0.9
    print(f"Witaj emerycie, Twoja opłata za {liczba_nocy} nocy wynosi: {oplata:.2f}zł")


