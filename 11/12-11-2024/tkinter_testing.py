import tkinter as tk
from tkinter import ttk

def CallBottone():
    print("Bottone chiamato!")
    print(entryInt.get()) # prende l'input sottoforma di numero


# window
window = tk.Tk()
window.title("Tkinter testing")
window.geometry("300x150")

# title
title_label = ttk.Label(master = window, text = "Widget label", font="Calibri, 24 bold")
title_label.pack()

# input field
input_frame = ttk.Frame(master = window)

entryInt = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable= entryInt)
button = ttk.Button( master = input_frame, text = "Bottone", command = CallBottone)

# impacchetta la roba 
entry.pack(side = "left", padx= 20)
button.pack(side = "left")
input_frame.pack(pady = 10)

#run
window.mainloop()