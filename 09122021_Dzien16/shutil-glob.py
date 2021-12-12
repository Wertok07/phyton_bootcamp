"""
Operacje "wysokopoziomowe" na plikach/katalogach i wyszukiwanie
"""
import glob, shutil

#files = glob.glob("/Users/Macbook/PycharmProjects/phyton_bootcamp/09112021_Dzien09/*.txt")
#files = glob.glob("../09112021_Dzien09/*.txt")
#files = glob.glob("../??122021_Dzien??/*")
import os.path

files = glob.glob("../**/*.py")
#files = glob.glob("/Users/Macbook/PycharmProjects/phyton_bootcamp/**/*.py")
for file in files:
    print(file)

## SHUTIL - wysokopoziomowe operacje na plikach

#shutil.copy(files[0], "./tmp")
#shutil.move(files[1], "./tmp")
dst_file = os.path.join("./tmp", os.path.basename(files[9]))
print(dst_file)