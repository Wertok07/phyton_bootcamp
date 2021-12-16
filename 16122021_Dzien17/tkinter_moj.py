import tkinter

def funkcja():
    print("Kloc poleciał!!!!!!!")

root = tkinter.Tk()

root.title("Nastawnik")

a_entry = tkinter.Entry(master=root)
a_entry.pack()

a_label = tkinter.Label(master=root, text="trE")
a_label.pack()

dsfsd = tkinter.Button(master=root, text="Kupa", command=funkcja)
dsfsd.pack()

root.mainloop()