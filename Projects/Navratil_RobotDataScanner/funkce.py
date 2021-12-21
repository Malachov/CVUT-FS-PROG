import pandas as pd

def changer(kod: int, soubor: str) -> str:
    if soubor == "recording":
        setup = recording (kod)
    else:
        setup = find_tab("program/"+soubor+".csv", kod)
    return setup

def find_tab(tabulka: str, cisloradku: int) -> str:
    # funkce hleda v danem souboru csv
    # vstup = nazev souboru, cislo radku
    # vystup = hodnota na hledanem radku
    seznam = pd.read_csv(tabulka, index_col=None, dtype=str)  # header=None,
    seznam.set_index("id", inplace=True)
    try :
        vysledek = seznam.loc[cisloradku, "nazev"]

        return vysledek

    except FileNotFoundError:
        print("Chybi soubor s touto tridou prikazu!")
        return "neni"

    except KeyError:
        print("Prikaz neni definovan!")
        return "neni"

def recording(kod: int) -> bool:
    try:
        if kod == "0001":
            nahravani = True
            
        elif kod == "0002":
            nahravani = False
             
        return nahravani

    except UnboundLocalError:
        print("neznamy kod pro nahravani!")
        return "neni"



