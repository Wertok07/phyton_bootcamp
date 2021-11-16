import sys

slownik = dict()  # albo slownik = {}


def sorted_func(x):
    napis1, napis2 = x[0].split("-")
    return int(napis2)


def sorted_func2(x):
    return int(x[1])


try:
    argument = sys.argv[1]
    with open(argument) as fd:
        for line in fd:
            wartosc = 0
            name, action, time = line.strip().split(";")
            time = int(time)
            if action == "LOGIN":
                wartosc = slownik.setdefault(name, 0)
                slownik[name] = wartosc - time
            else:
                wartosc = slownik.setdefault(name, 0)
                slownik[name] = wartosc + time
    print("*" * 20, " Po nazwie ", "*" * 20)
    for ki, va in sorted(slownik.items(), key=sorted_func, reverse=True):
        print(f' - {ki}: {va} s')
    print("*" * 20, " Po czasie ", "*"*20)
    for ki, va in sorted(slownik.items(), key=lambda x: x[1], reverse=True):  # key=lambda x: x[1] or key=sorted_func2
        print(f' - {ki}: {va} s')
except IndexError:
    print("Nie podano argumentu")
except FileNotFoundError:
    print("Nie istnieje taki plik")
