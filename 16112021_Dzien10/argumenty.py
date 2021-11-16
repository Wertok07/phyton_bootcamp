import sys
import os.path

# sys.argv.index(1)
try:
    argumenty = sys.argv[1]
except IndexError:
    print("Nie podano nazwy pliku")

if len(sys.argv) == 2:
    argumenty = sys.argv[1]
    if os.path.exists(argumenty):
        with open(argumenty, "rt") as fd:
            for linianum, text in enumerate(fd, start=1):
                print(linianum, ": ", text, sep="", end="") #linia zawiera znak nowej lini
