"""
Napisać funkcję kopiującą pliki z bieżącego katalogu.
Sprawdzać czy plik źrodłowy i docelowy nie mają takiej samej nazwy.
Użyć context manager'a
def copy(src: str, dst: str) -> str:
    pass
"""

def copy(src, dst):
    with open(src, "wb") as srcfd, open(dst, "wb") as dstfd:
        pass
    # src - plik zrodlowy
    # dst - plik docelowy
    pass