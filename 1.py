import tkinter as tk
from tkinter import font

root = tk.Tk()
available_fonts = font.families()
print(available_fonts)
root.destroy()
