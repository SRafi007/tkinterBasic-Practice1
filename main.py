import tkinter as tk
from tkinter import *

window=tk.Tk()
windowWidth=window.winfo_screenwidth()
windowHeight=window.winfo_screenheight()
window.geometry(f'{windowWidth}x{windowHeight}+0+0')
msg=tk.Label(text="my first tkinter window",background="Red")
entry=tk.Entry()
btn=tk.Button(text="Button")
msg.pack()
entry.pack()
btn.pack()

window.mainloop()