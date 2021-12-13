# TODO ukol
#
# - 1) podle ostatnich cisel vlozit parametry do funkce
# - 2) Vytvorit objekt robota z skriptu main a zavolat prislusnou funci s parametry

import pandas as pd

def findtab(tabulka, cisloradku):
    # funkce hleda v danem souboru csv
    # vstup = nazev souboru, cislo radku
    # vystup = hodnota na hledanem radku
    seznam = pd.read_csv(tabulka, index_col=None, dtype=str)  # header=None,
    seznam.set_index("id", inplace=True)
    if (seznam.index == cisloradku).any():
        vysledek = seznam.loc[cisloradku, "nazev"]
        
    else:
        print ("Chybi zaznam o tomto prikazu!")
        vysledek = None
    return vysledek

def scanner_change(kod):
    setup = findtab("program/scanner_change.csv", kod)
    print("nastaveni zmeneno na " + setup )
    
    return setup


def ref_point_change(kod):
    setup = findtab("program/ref_point_change.csv", kod)
    print("nastaveni zmeneno na " + setup )
    
    return setup

def gripper_change(kod):
    gripper = findtab("program/gripper_change.csv", kod)
    #if gripper == None:

    print("gripper zmenen na " + gripper )
    
    return gripper

def recording(kod):
    if kod == "0001":
        nahravani = True
        print("nahravani zapnuto")
    elif kod == "0002":
        nahravani = False
        print("nahravani vypnuto")
    else:
        print ("neznamy kod pro nahravani")
    
    return nahravani


class Robot:
    def __init__(self, CODE="Default") -> None:
        self.CODE = CODE

        self.function_part = self.CODE[0:2]
        self.parameter_1_part = self.CODE[2:6]

        function_name = self.orders_dict[self.function_part]
        self.used_function = self.function_dict[function_name]

        self.attribute=self.attribute_dict[function_name]

        #self.recording=recording("0002")
        #self.gripper=gripper_change("0001")
        #self.scanner=scanner_change("0001")
        #self.ref_point=ref_point_change("0001")

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
        self.used_function(self.parameter_1_part)


#robot_orders = Robot("01")
#robot_orders_2 = Robot("02")
vozitko = Robot ("030008")
vozitko.run()
#testovani2 = Robot ("040001")

#testovani2.run()
#robot_orders.run()


a = 8
