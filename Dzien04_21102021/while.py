"""
Pętla while
"""
counter = 10

while counter > 0:
    counter -= 1
    print(counter)
    if counter == 5:
        break

while 1:
    liczba = input("Podaj liczbe do 10 bądź większą bądź równą 100: ")
    liczba = int(liczba)
    if liczba < 10 or liczba >= 100:
        break