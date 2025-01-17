import tkinter as tk
from tkinter import Tk, Entry, Button, Label, StringVar

Window = tk.Tk()
Window.geometry("600x250")
Window.title("Efik Dictionary")
welcome_label = tk.Label(Window, text="Welcome to my Dictionary", padx=200, pady=50, bg= "grey", fg="white", font="impact 16")
welcome_label.pack()

title_label = tk.Label(Window, text="Please select a language")
title_label.pack(pady=10)

word_label = tk.Label(Window, text="Enter a word:")
word_label.pack()

entry_text = Entry(Window)
entry_text.pack()

result = StringVar()
result_label = Label(Window, textvariable=result)
result_label.pack()

efik_dict = {
              "hello": "mokom",
              "thank you": "sosono",
              "house": "kasahorow",
              "sorry": "inin",
              "water": "moN",
              "money": "okpoho",
              "farm": "ntie",
              "God": "abasi",
              "child": "nwanan",
              "mother": "mme",
              "father": "idiok",
              "come": "di",
            }

def efik(word):
    if word in efik_dict:
        result.set(efik_dict[word.lower()])
        print(efik_dict[word.lower()])
    else:
        result.set("Not found")
        print("Not found")

efik_btn = Button(Window, bg="maroon" ,text="Efik",fg="white",padx=20 ,pady=5, command=lambda: efik(entry_text.get()))
efik_btn.pack()


Window.mainloop()
