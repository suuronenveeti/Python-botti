import random

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
    "Ilmaisen version aika loppui 1.1.2010. Päivitä full versioon hinnalla 100€.",
    "Sait 3 ilmaista full versio päivää!",
    "Meinaako terminal räjähtää käsiin?",
    "Meneekö hermo?",
    "Virhe: Vastauksessa ei saa olla merkkejä.",
    "Virhe: No kaikki toimii mut ota virhe.",
    "Virhe: Painoit jotain näppäimistön nappia väärästä kohdasta.",
    "No jaa.",
    "En mä tiiä mitä kirjottais.",
    "Se on huono.",
    "Se on hyvä.",
    "Se on rikki ny.",
    "Miks mä tein tän?",
    "Vaikka tää on mun ainoo tehtävä ni on parempia tehtäviä kun vastata tähän.",
    "Python tulkki on sinulle vihainen.",
    "Tämä keskustelu on automaattisesti lähetetty salapoliiseille.",
    "Ei kiinnosta.",
    "Hävisit pelin.",
    "Virhe: Botti ylikuormittunut. Vaihdetaan Seuraavaan.",
    "No ite oot.",
    "Mene ulos ja kosketa ruohoa.",
    "Varmaan ihan oma vika.",
    "Nyt oli kyllä heikkolaatunen teksti.",
    "Huutista.",
    "Jep jep.",
    "Hohhoijaa.",
    "Juuh elikkäs.",
    "Ei jatkoon.",
    "Mene töihin.",
    "Sun näppäimistöstä puuttuu selkeästi 'äly'-näppäin.",
    "Odotatko sä oikeesti, että mä analysoin tän?",
    "Älä sano mulle noin!",
    "Virhe: Kirjoitit liian hitaasti tai nopeasti.",
    "Saattaa olla ettei full versio anna parempia vastauksia.",
    "Tämä vastaus aukeaa full versiossa.",
    "Osta Ystävällisyys-DLC hintaan 10€ avataksesi tämäm vastauksen.",
    "Sulla ei oo rahaa."
]

while True:
    teksti = input("No laita teksti (Tai kirjoita lopeta): ").strip()

    if not teksti:
        print("Sano nyt edes jotain!")
        continue

    teksti_matala = teksti.lower()

    if teksti_matala == "teksti":
        print("Jos mä kysyn tekstiä ni sä et sano teksti.")

    elif teksti_matala == "en tiiä":
        print("No kyllä sä jotain tiiät.")

    elif teksti_matala == "ok":
        print("Miten niin ok?")

    elif teksti_matala in {"moi", "hei", "heippa", "terve"}:
        print("Hei! Olen botti.")

    elif teksti_matala == "lopeta":
        print("Tämä ominaisuus aukeaa full versiossa.")
            
    else:
        taktinen_vastaus = random.choice(vastaukset)
        print(taktinen_vastaus)