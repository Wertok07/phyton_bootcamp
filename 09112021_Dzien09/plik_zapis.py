"""
Zapis plików w pytongu
"""

fd = open("do-zapisu.txt", "at")

fd.write("Linia 1\n")
fd.write("Linia 2\n")
fd.writelines(["Linia A", "\n", "Linia B", "\n"])

fd.close()
