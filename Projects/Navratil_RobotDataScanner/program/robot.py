# TODO ukol
#
# - 1) podle ostatnich cisel vlozit parametry do funkce
# - 2) Vytvorit objekt robota z skriptu main a zavolat prislusnou funci s parametry

import pandas as pd


def find_tab(tabulka, cisloradku) -> str:
    # funkce hleda v danem souboru csv
    # vstup = nazev souboru, cislo radku
    # vystup = hodnota na hledanem radku
    seznam = pd.read_csv(tabulka, index_col=None, dtype=str)  # header=None,
    seznam.set_index("id", inplace=True)
    if (seznam.index == cisloradku).any():
        vysledek = seznam.loc[cisloradku, "nazev"]

        return vysledek

    else:
        raise FileNotFoundError("Chybi zaznam o tomto prikazu!")


def scanner_change(kod):
    setup = find_tab("program/scanner_change.csv", kod)
    print("nastaveni zmeneno na " + setup)

    return setup


def ref_point_change(kod):
    setup = find_tab("program/ref_point_change.csv", kod)
    print("nastaveni zmeneno na " + setup)

    return setup


def gripper_change(kod):
    gripper = find_tab("program/gripper_change.csv", kod)
    # if gripper == None:

    print("gripper zmenen na " + gripper)

    return gripper


def recording(kod):
    if kod == "0001":
        nahravani = True
        print("nahravani zapnuto")
    elif kod == "0002":
        nahravani = False
        print("nahravani vypnuto")
    else:
        print("neznamy kod pro nahravani")

    return nahravani


class Robot:
    def __init__(self) -> None:
        self._config_me = 8
        pass

        # self.recording=recording("0002")
        # self.gripper=gripper_change("0001")
        # self.scanner=scanner_change("0001")
        # self.ref_point=ref_point_change("0001")

    orders_dict = {
        "01": "scanner_change",
        "02": "ref_point_change",
        "03": "gripper_change",
        "04": "recording",
    }

    function_dict = {
        "scanner_change": scanner_change,
        "ref_point_change": ref_point_change,
        "gripper_change": gripper_change,
        "recording": recording,
    }

    attribute_dict = {
        "scanner_change": "scanner",
        "ref_point_change": "ref_point",
        "gripper_change": "gripper",
        "recording": "recording",
    }

    def run(self):
        setattr(self, self.attribute, self.used_function(self.parameter_1_part))

    def change_configuration(self, CODE):
        self.CODE = CODE

        self.function_part = self.CODE[0:2]
        self.parameter_1_part = self.CODE[2:6]

        self.function_name = self.orders_dict[self.function_part]
        self.used_function = self.function_dict[self.function_name]

        self.attribute = self.attribute_dict[self.function_name]


robot = Robot()
