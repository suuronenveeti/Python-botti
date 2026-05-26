import random

while True:
    teksti = input("No laita teksti: ").strip()

    if not teksti:
        print("Sano nyt edes jotain!")
        continue

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
            "No ei tota osaa edes lukea kun on niin sotkuinen.",
            "Oletko itse vähän työtön?",
            "Tämä vastaus aukeaa tasolla 100.",
            "Ei oikeesti!",
            "Onko tämä edes mahdollista?",
            "Nyt on kyllä paha.",
            "Tekstisi rikkoo sääntöjä.",
            "Olet saanut yhden kolikon.",
            "Tämä vastaus maksaa 5€ kuukaudessa.",
            "Vinkki: En muista monta kolikkoa olet saanut.",
            "Vinkki: Et saa seuraavaa tasoa koskaan enkä edes muista millä tasolla olet.",
            "Vinkki: Et osaa maksaa kuukausimaksua.",
            "Teksti oli niin huono että minä hermostun.",
            "Tarkistin tiedoista ja kukaan ei kysynyt.",
            "Vinkki: Ilmaisen version aika loppui 1.1.2010. Päivitä full versioon hinnalla 100€.",
            "Sait 3 ilmaista full versio päivää!"

        ]

        taktinen_vastaus = random.choice(vastaukset)
        print(taktinen_vastaus)