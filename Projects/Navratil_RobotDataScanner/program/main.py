import pandas as pd
from program import RobotOrders


def findtab(tabulka, cisloradku):
    # funkce hleda v danem souboru csv
    # vstup = nazev souboru, cislo radku
    # vystup = hodnota na hledanem radku
    seznam = pd.read_csv(tabulka, index_col=None, dtype=str)  # header=None,
    seznam.set_index("id", inplace=True)
    vysledek = seznam.loc[cisloradku, "nazev"]
    return vysledek


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
        print("To by mohlo jit")

        trida = scan[:2]
        # vzhledani tridy pomoci fce find
        check = pd.read_csv("program/main.csv", index_col=None, dtype=str)
        if (check.index == trida).any():
            print("Tato trida neexistuje!")
        else:
            sekundar = findtab("program/main.csv", trida)
            print(sekundar)
            print(scan[2:])

            check = pd.read_csv("program/" + sekundar + ".csv", index_col=None, dtype=str)
            if (check.index == sekundar).any():
                print("Tento prikaz neexistuje!")
            else:
                prikaz = findtab("program/" + sekundar + ".csv", scan[2:])
                print(prikaz)
                if prikaz[:2] == "00":
                    prikaz[2:] + "()"


print("Program byl uspesne ukoncen")
