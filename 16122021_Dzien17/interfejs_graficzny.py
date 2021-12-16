import tkinter
from tkinter import messagebox


def policz_sume():
    try:
        a = int(a_entry.get())
        b = int(b_entry.get())
        wynik_label.configure(text=f'Wynik: {a + b}')
    except ValueError:
        messagebox.showerror('Błędne dane!', 'Musisz wprowadzić wartości liczbowe!')


root = tkinter.Tk()
#root.geometry("800x480")
root.columnconfigure(1, weight=1)
a_label = tkinter.Label(master=root, text='Liczba a:')
a_label.grid(row=0, column=0)
a_entry = tkinter.Entry(master=root)
a_entry.grid(row=0, column=1, sticky=tkinter.EW)
b_label = tkinter.Label(master=root, text='Liczba b:')
b_label.grid(row=1, column=0)
b_entry = tkinter.Entry(master=root)
b_entry.grid(row=1, column=1, sticky=tkinter.EW)
policz_button = tkinter.Button(master=root, text='Policz', command=policz_sume)
policz_button.grid(row=3, column=0)
wynik_label = tkinter.Label(master=root, text='Wynik: - ')
wynik_label.grid(row=3, column=1, sticky=tkinter.EW)
root.title('Sumator')
#root.attributes("-fullscreen", True)
root.mainloop()