"""
Korzystanie z pliku przy uzyciu kontkst menagera
"""

with open("text.txt", "rt") as fd:
    s = fd.read()
    print(s)
    print(fd.closed)
print(fd.closed)

# zapis do pliku binarnego
with open("test.bin", "wb") as fd:
    tablica = bytearray([87,111,106,116,101,107])
    fd.write(tablica)
    fd.flush()

"""
Zadanie domowe - napisać funckcje ktora kopiuje plik
"""

def copy(src, dst):
    with open(src, "wb") as srcfd, open(dst, "wb") as dstfd:
        pass
    # src - plik zrodlowy
    # dst - plik docelowy
    pass


