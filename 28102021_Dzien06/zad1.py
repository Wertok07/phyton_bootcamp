#string = "Ala <ma kota>, a kot ma Alę"

# bool = False
# wypisuje = ""
#
# for slowo in string:
#     if("<" == slowo):
#         bool = True
#         continue
#     if(">" == slowo):
#         bool = False
#     if(bool):
#         wypisuje += slowo
# print(len(wypisuje))

#print(string.find('>') - string.find('<') -1)

text = input("Podaj tekst: ")
slownik = {}

for litera in text:
    slownik.setdefault(litera, 0)
    slownik[litera] += 1
print(slownik)