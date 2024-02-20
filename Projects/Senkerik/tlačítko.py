import tkinter as tk
from random import randint

def clicked_yes():
    label.config(text="Díky")
    yes_button.destroy()
    no_button.destroy()
    no_button.place(x=randint(0, 350), y=randint(0, 350))

def clicked_no():
    new_x = no_button.winfo_x() + randint(-70, 70)
    new_y = no_button.winfo_y() + randint(-70, 70)

    # Zkontrolujeme, zda nové souřadnice zůstávají uvnitř okna
    if 0 <= new_x <= 450 and 0 <= new_y <= 350:
        no_button.place(x=new_x, y=new_y)

root = tk.Tk()
root.geometry("500x400")

label = tk.Label(root, text="Dostanu zápočet?", font=("Helvetica", 20))
label.pack()

yes_button = tk.Button(root, text="Ano", width=10, font=("Helvetica", 16), command=clicked_yes, bd=5, relief="raised")
yes_button.pack(side="left", padx=50)

no_button = tk.Button(root, text="Ne", width=10, font=("Helvetica", 16), command=clicked_no, bd=5, relief="raised")
no_button.pack(side="left", padx=50)

root.mainloop()