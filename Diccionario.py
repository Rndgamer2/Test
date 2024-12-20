meme_dict = {
            "FR": "Es una abreviatura en ingles de que algo es cierto o estas de acuerdo",
            "MMG": "Una forma de insulto hacia una persona",
            "YTS": "Cuando estas de acuerdo con algo o una accion"
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("No existe esta palabra")
