import sys

slownik = dict() # set() zbiory przechowują tylko unikalne elementy

try:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
except IndexError:
    print("Lepiej te argumenty dobieraj ziomuś")

with open(arg1) as fd1, open(arg2, "w") as fd2:
    for maile_wej in fd1:
        maile_wej = maile_wej.lower().strip()
        if maile_wej.find("@") != -1 and maile_wej.count("@") == 1:
            slownik.setdefault(maile_wej, None)
    for k, v in slownik.items():
        print(k)
        fd2.write(f"{k}\n")