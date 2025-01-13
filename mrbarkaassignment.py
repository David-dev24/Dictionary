import tkinter as tk
from tkinter import Tk, Entry, Button, Label, StringVar

Window = tk.Tk()
Window.geometry("600x250")
Window.title("Naija Dictionary")
welcome_label = tk.Label(Window, text="Welcome to our Dictionary", padx=200, pady=50, bg= "maroon", fg="white", font="impact 16")
welcome_label.pack()
Window.geometry("600x600")

title_label = tk.Label(Window, text="Please select a language")
title_label.pack(pady=10)

word_label = tk.Label(Window, text="Enter a word:")
word_label.pack()

entry_text = Entry(Window)
entry_text.pack()

result = StringVar()
result_label = Label(Window, textvariable=result)
result_label.pack()

hausa_dict = {
              "hello": "sannu",
              "thank you": "na gode",
              "house": "gida",
              "sorry": "yi hakuri",
              "water": "ruwa",
              "money": "kudi",
              "boy": "yaro",
              "girl": "yarinya",
              "one": "daya",
              "ten": "goma",
              "food": "abinci",
              "sea": "teku",
              "eye": "ido",
              "nose": "haci",
              "farm": "gona",
              "God": "allah",
              "child": "yaya",
              "mother": "uwa",
              "father": "uba",
              "come": "zo",
            }

igbo_dict = {
              "hello": "nnoo",
              "thank you": "imela",
              "house": "ulo",
              "sorry": "ndo",
              "water": "mmiri",
              "money": "ego",
              "boy": "nwoke",
              "girl": "nwanyi",
              "one": "otu",
              "ten": "iri",
              "food": "nri",
              "sea": "osimiri",
              "eye": "anya",
              "nose": "imi",
              "farm": "ugbo",
              "God": "chineke",
              "child": "nwata",
              "mother": "nne",
              "father": "nna",
              "come": "bia",
           }

yoruba_dict = {
              "hello": "bawo",
              "thank you": "edupe",
              "house": "ile",
              "sorry": "pele",
              "water": "omi",
              "money": "owo",
              "boy": "omokunri",
              "girl": "omobirin",
              "one": "okan",
              "ten": "mewaa",
              "food": "ounje",
              "sea": "okun",
              "eye": "oju",
              "nose": "imu",
              "farm": "oko",
              "God": "olorun",
              "child": "omode",
              "mother": "iya",
              "father": "baba",
              "come": "wa",
             }

igala_dict = {
              "hello": "agba",
              "thank you": "awa",
              "house": "unyi",
              "sorry": "nago",
              "water": "omi",
              "money": "oko",
              "boy": "okolobia",
              "girl": "igbele",
              "one": "oka",
              "ten": "egwa",
              "food": "ujewun",
              "sea": "okun",
              "eye": "eku",
              "nose": "imo",
              "farm": "oko",
              "God": "ojo",
              "child": "oma",
              "mother": "oja",
              "father": "atah",
              "come": "lia",
             }

efik_dict = {
              "hello": "mokom",
              "thank you": "sosono",
              "house": "kasahorow",
              "sorry": "inin",
              "water": "moN",
              "money": "okpoho",
              "boy": "okon",
              "girl": "nwan",
              "one": "kiet",
              "ten": "doup",
              "food": "nkukwo",
              "sea": "ndem",
              "eye": "anya",
              "nose": "eso",
              "farm": "ntie",
              "God": "abasi",
              "child": "nwanan",
              "mother": "mme",
              "father": "idiok",
              "come": "di",
            }



def hausa(word):
    if word in hausa_dict:
        result.set(hausa_dict[word.lower()])
        print(hausa_dict[word.lower()])
    else:
        result.set("Not found")
        print("Not found")

def igbo(word):
    if word in igbo_dict:
        result.set(igbo_dict[word.lower()])
        print(igbo_dict[word.lower()])
    else:
        result.set("Not found")
        print("Not found")


def yoruba(word):
    if word in yoruba_dict:
        result.set(yoruba_dict[word.lower()])
        print(yoruba_dict[word.lower()])
    else:
        result.set("Not found")
        print("Not found")


def igala(word):
    if word in igala_dict:
        result.set(igala_dict[word.lower()])
        print(igala_dict[word.lower()])
    else:
        result.set("Not found")
        print("Not found")


def efik(word):
    if word in efik_dict:
        result.set(efik_dict[word.lower()])
        print(efik_dict[word.lower()])
    else:
        result.set("Not found")
        print("Not found")




hausa_btn = Button(Window, bg="maroon", text="Hausa",fg="white", padx=20 ,pady=5, command=lambda: hausa(entry_text.get()))
hausa_btn.pack()

igbo_btn = Button(Window, bg="maroon",text="Igbo",fg="white", padx=20 ,pady=5,command=lambda: igbo(entry_text.get()))
igbo_btn.pack()


yoruba_btn = Button(Window, bg="maroon", text="Yoruba",fg="white", padx=20 ,pady=5, command=lambda: yoruba(entry_text.get()))
yoruba_btn.pack()


igala_btn = Button(Window, bg="maroon" ,text="Igala",fg="white",padx=20 ,pady=5, command=lambda: igala(entry_text.get()))
igala_btn.pack()


efik_btn = Button(Window, bg="maroon" ,text="Efik",fg="white",padx=20 ,pady=5, command=lambda: efik(entry_text.get()))
efik_btn.pack()




Window.mainloop()








