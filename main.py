from io import BytesIO
import tkinter as tk
import pypokedex
import PIL.Image
import PIL.ImageTk
import urllib3

pokemon = pypokedex.get(name="charmander")
# print(pokemon.dex)
# print(pokemon.name)
# print(pokemon.abilities)
# print(pokemon.types)
# print(pokemon.sprites.front.get("default"))

window = tk.Tk()
window.geometry("600x500")
window.title("pokedex")
window.config(padx=10, pady=10)

title_label = tk.Label(window, text="Parra Pokedex")
title_label.config(font=("Ariel", 32))
title_label.pack(padx=10, pady=10)

pokemon_image = tk.Label(window)
pokemon_image.pack()

pokemon_information = tk.Label(window)
pokemon_information.config(font=("Ariel", 20))
pokemon_information.pack(padx=10, pady=10)

pokemon_types = tk.Label(window)
pokemon_types.config(font=("Ariel", 20))
pokemon_types.pack(padx=10, pady=10)


def load_pokemon():
    pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))

    http = urllib3.PoolManager()
    response = http.request("GET", pokemon.sprites.front.get("default"))
    image = PIL.Image.open(BytesIO(response.data))

    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image=img)
    pokemon_image.image = img

    pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}")
    pokemon.types.config(text=f"{pokemon.types}")


label_id_name = tk.Label(window, text="ID or name")
label_id_name.config(font=("Arial", 20))
label_id_name.pack(padx=10, pady=10)

text_id_name = tk.Text(window, height=1)
text_id_name.config(font=("Arial", 20))
text_id_name.pack(padx=10, pady=10)

btn_load = tk.Button(window, text="Load Pokemon", command=load_pokemon)
btn_load.config(font=("Ariel", 20))
btn_load.pack(padx=10, pady=10)

window.mainloop()
