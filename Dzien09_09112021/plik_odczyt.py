"""
Obsługa odczytu plików w Pythonie
"""

fd = open("text.txt", "rt")
# s = fd.read()
s2 = fd.read(20)
fd.seek(1)  # ustawienie wskaźnika odczytu pliku
s3 = fd.read(10)

fd.seek(0)
# print("-"*50)
while True:
    s = fd.readline()
    if len(s) == 0:
        break
    # print(s.strip())
# print("2-----------------")

fd.seek(0)  # Odczyt lini do listy
lista = fd.readlines()
print(lista)
lista = [s.strip() for s in lista]
print(lista)
lista = [s.strip() for s in lista if len(s)>12]
print(lista)

# iteracja po file descriptorze
fd.seek(0)
for fds in fd:
    print(fds.strip())

fd.close()
# print(s2, s3, sep="\n")
