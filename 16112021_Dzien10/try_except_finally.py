try:
    f = open("ssjkhdas")
except FileNotFoundError:
    print("Except")
finally:
    f.close()