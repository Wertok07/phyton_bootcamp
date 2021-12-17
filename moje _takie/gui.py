import tkinter
import customtkinter

root = tkinter.Tk()

root.title("Nastawnik")
root.geometry("480x800")

frame = customtkinter.CTkButton(master=root, width=230, height=100, corner_radius=10, text="User-Button 1")
frame.place(relx=0.0, rely=0.1, anchor=tkinter.W)
# frame.grid(row=0, column=1)

frame1 = customtkinter.CTkButton(master=root, width=230, height=100, corner_radius=10, text="User-Button 2")
frame1.place(relx=0.5, rely=0.1, anchor=tkinter.W)
# frame1.grid(row=1, column=0)

frame2 = customtkinter.CTkButton(master=root, width=230, height=100, corner_radius=10, text="User-Button 3")
frame2.place(relx=0.01, rely=0.9, anchor=tkinter.W)
# frame2.grid(row=1, column=1)

frame3 = customtkinter.CTkButton(master=root, width=230, height=100, corner_radius=10, text="User-Button 4")
frame3.place(relx=0.51, rely=0.9, anchor=tkinter.W)
# frame3.grid(row=0, column=0)

frame4 = customtkinter.CTkButton(master=root, width=70, height=100, corner_radius=10, text="-", text_font=("latoregular", 30))
frame4.place(relx=0.05, rely=0.3, anchor=tkinter.W)
# frame4.grid(row=1, column=0)

frame5 = customtkinter.CTkButton(master=root, width=70, height=100, corner_radius=10, text="+", text_font=("latoregular", 30))
frame5.place(relx=0.8, rely=0.3, anchor=tkinter.W)
# frame5.grid(row=1, column=1)

label = customtkinter.CTkLabel(master=root, text="21.5°C", width=280, height=100, corner_radius=10, text_font=("latoregular", 90))
label.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

frame5 = customtkinter.CTkButton(master=root, width=70, height=100, corner_radius=10, text="+", text_font=("latoregular", 30))
frame5.place(relx=0.8, rely=0.3, anchor=tkinter.W)
# frame5.grid(row=1, column=1)

root.mainloop()
