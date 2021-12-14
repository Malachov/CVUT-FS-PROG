import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.filedialog import askopenfilename
from pydub import AudioSegment
from tkinter.ttk import *


# root window
root = tk.Tk()
root.geometry('400x300')
root.resizable(False, False)
root.title('Music converter')

l = tk.Label(root, bg='white', width=20, text='zvolte vysledny format')
l.pack()
def nahrat():
    tk.Tk().withdraw() # part of the import if you are not using other tkinter functions
    fn = askopenfilename()
    song = AudioSegment.from_file(fn)
    if formaty.get()=="mp3":
        song.export("export.mp3", format="mp3")  

    elif formaty.get()=="mp4":
        song.export("export.mp4", format="mp4") 

    elif formaty.get()=="wav":
        song.export("export.wav", format="wav") 
        
    elif formaty.get()=="ogg":
        song.export("export.ogg", format="ogg") 

       


formaty = tk.StringVar()
sizes = (('mp3', 'mp3'),
         ('mp4', 'mp4'),
         ('wav', 'wav'),
         ('ogg', 'ogg'))

# label
label = ttk.Label(text="Choose final format")
label.pack(fill='x', padx=5, pady=5)

# radio buttons
for size in sizes:
    r = ttk.Radiobutton(
        root,
        text=size[0],
        value=size[1],
        variable=formaty
    )
    r.pack(fill='x', padx=5, pady=5)

# button
button1 = ttk.Button(
    root,
    text="Nahrat soubor a exportovat",
    command=nahrat)


button1.pack(fill='x', padx=5, pady=5)

root.mainloop()
