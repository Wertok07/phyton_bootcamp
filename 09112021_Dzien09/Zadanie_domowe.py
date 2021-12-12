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
    with open(src, "rb") as srcfd, open(dst, "wb") as dstfd:
        for i in srcfd:
            dstfd.write(i)
    return "Udało sie, plik skopiowany!"

print(copy("text.txt","grudzien.txt"))