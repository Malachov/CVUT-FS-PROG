import pandas as pd
from robot import Robot


def findtab(tabulka, cisloradku):
    # funkce hleda v danem souboru csv
    # vstup = nazev souboru, cislo radku
    # vystup = hodnota na hledanem radku
    seznam = pd.read_csv(tabulka, index_col=None, dtype=str)  # header=None,
    seznam.set_index("id", inplace=True)
    vysledek = seznam.loc[cisloradku, "nazev"]
    return vysledek

print("spousteni programu v zakladnim nastaveni")
prikaz=Robot("010001")
prikaz.run()
prikaz=Robot("020001")
prikaz.run()
prikaz=Robot("030001")
prikaz.run()
prikaz=Robot("040002")
prikaz.run()

while True:
    scan = input("Zadej sestimistny kod:")

    if scan == "000000":
        Konec = input("Nacten ukoncovaci kod. Program se nyni ukonci: (Y/N)")
        if Konec == "Y" or Konec == "y":
            print("zvoleno ukonceni programu, nashledanou")
            break
        else:
            print("Program dale pokracuje")
    elif len(scan) != 6:
        print("Spatny format cisla!")
    else:
        #print("To by mohlo jit")
        prikaz=Robot(scan)
        prikaz.run()

        


print("Program byl uspesne ukoncen")
