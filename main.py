import random

while True:
    teksti = input("No laita teksti: ")

    if teksti.lower() == "teksti":
        print("Jos mä kysyn tekstiä ni sä et sano teksti.")

    elif teksti.lower() == "en tiiä":
        print("No kyllä sä jotain tiiät.")

    elif teksti.lower() == "ok":
        print("Miten niin ok?")

    else:
        vastaukset = [
            "Taktinen.",
            "Ok.",
            "Ei tälläsiä!",
            "Joo.",
            "Ei.",
            "Nyt on kyllä hullu!",
            "Noni.",
            "No ei tota osaa edes lukea kun on niin sotkuinen."
        ]

        taktinen_vastaus = random.choice(vastaukset)
        print(taktinen_vastaus)