import tkinter
from tkinter import messagebox


def policz_koszty():
    dystans = float(dystans_entry.get())
    spalanie = float(spalanie_entry.get())
    cena = float(cena_entry.get())
    osoby = int(os_entry.get())

    koszty = (dystans / 100) * spalanie * cena
    wynik_label.configure(text=f"Suma: {koszty} zł")
    wynik_label2.configure(text=f"Na łebka: {koszty/osoby} zł")




root = tkinter.Tk()
root.title("Kalkulator podróży")

root.columnconfigure(1, weight=1)

dystans_label = tkinter.Label(master=root, text="Dystans [km]: ")
dystans_label.grid(row=0, column=0)
dystans_entry = tkinter.Entry(master=root)
dystans_entry.grid(row=0, column=1)

spalanie_label = tkinter.Label(master=root, text="Śr spalanie [l/100km]: ")
spalanie_label.grid(row=1, column=0)
spalanie_entry = tkinter.Entry(master=root)
spalanie_entry.grid(row=1, column=1)

cena_label = tkinter.Label(master=root, text="Cena paliwa [l]: ")
cena_label.grid(row=2, column=0)
cena_entry = tkinter.Entry(master=root)
cena_entry.grid(row=2, column=1)

os_label = tkinter.Label(master=root, text="Osoby [os]: ")
os_label.grid(row=3, column=0)
os_entry = tkinter.Entry(master=root)
os_entry.grid(row=3, column=1)

button = tkinter.Button(master=root, text="Weź mnie to policz!", command=policz_koszty)
button.grid(row=4, column=1)

wynik_label = tkinter.Label(master=root)
wynik_label.grid(row=5, column=1)

wynik_label2 = tkinter.Label(master=root)
wynik_label2.grid(row=6, column=1)

root.mainloop()
