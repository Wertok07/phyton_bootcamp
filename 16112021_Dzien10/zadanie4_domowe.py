import os

items = os.scandir(".")
for element in items:
    nazwa = element.name
    if nazwa.count(".") == 0:
        print(element.name)