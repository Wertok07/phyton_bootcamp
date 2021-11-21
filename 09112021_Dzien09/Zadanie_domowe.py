"""
Napisać funkcję kopiującą pliki z bieżącego katalogu.
Sprawdzać czy plik źrodłowy i docelowy nie mają takiej samej nazwy.
Użyć context manager'a
def copy(src: str, dst: str) -> str:
    pass
"""

def copy(src, dst):
    if src == dst:
        return "Pliki mają taką samą nazwe. Nie mogą miec!"
    with open(src, "rt") as srcfd, open(dst, "wt") as dstfd:
        for i in srcfd:
            dstfd.writelines(i.strip()+"\n")
    return "Udało sie, plik skopiowany!"
    # src - plik zrodlowy
    # dst - plik docelowy

print(copy("text.txt","tes.txt"))