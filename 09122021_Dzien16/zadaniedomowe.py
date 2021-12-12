"""
Napisać funckcje do rekursywnego kopiowania plików z jednego do innego katalogu
"""
import os

def copy(src, dst):
    if src == dst:
        return "Pliki mają taką samą nazwe. Nie mogą miec!"
    with open(src, "rb") as srcfd, open(dst, "wb") as dstfd:
        for i in srcfd:
            dstfd.write(i)
    return "Udało sie, plik skopiowany!"

def copy_tree(src, des):
    items = os.scandir(src)

    for item in items:
        sciezka_src = os.path.join(item)
        sciezka_des = os.path.join(des, item.name)
        if item.is_dir():
            os.mkdir(sciezka_des)
            copy_tree(sciezka_src, sciezka_des)
        else:
            copy(sciezka_src, sciezka_des)

copy_tree("/Users/Macbook/PycharmProjects/phyton_bootcamp/09122021_Dzien16/srcfolder", "/Users/Macbook/PycharmProjects/phyton_bootcamp/09122021_Dzien16/desfolder")


