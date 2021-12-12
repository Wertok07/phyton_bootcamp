"""
Tworzenie plików i katalogów tymczasowych
"""
import tempfile, os

print("Katalog tymczasowy dla systemu:", tempfile.gettempdir())
#Korzystanie z pliku tymczasowego

with tempfile.NamedTemporaryFile("wt", delete=True) as fd:
    print(fd.name)
    for _ in range(2000):
        fd.write("Ala ma kota\n")
        fd.write("Tomek ma raka\n")
    fd.write("Koniec tej magii")

print("Koniec istnienia pliku tmp")


with tempfile.TemporaryDirectory() as tmp_dir:
    print(tmp_dir)
    file_name = os.path.join(tmp_dir, "log.txt")
    with open(file_name, "wt") as fd:
        fd.write("0"*10_000)
        print("Koniec zapisu do pliku w katalogu tymczasowym")