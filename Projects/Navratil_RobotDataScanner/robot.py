# TODO ukol
#
# - 1) podle ostatnich cisel vlozit parametry do funkce
# - 2) Vytvorit objekt robota z skriptu main a zavolat prislusnou funci s parametry

from funkce import *


class Robot:
    def __init__(self) -> None:
        self.err=False
        pass

        self.recording=changer("0002", "recording")
        self.gripper=changer("0001", "gripper_change")
        self.scanner=changer("0001", "scanner_change")
        self.ref_point=changer("0001", "ref_point_change")

        self.parameters()

    orders_dict = {
        "01": "scanner_change",
        "02": "ref_point_change",
        "03": "gripper_change",
        "04": "recording",
    }


    attribute_dict = {
        "scanner_change": "scanner",
        "ref_point_change": "ref_point",
        "gripper_change": "gripper",
        "recording": "recording",
    }

    def run(self):
        if self.err == True:
            self.err=False
            print("Nastaveni zustalo bezezmeny! Stavajici nastaveni:")
        elif changer(self.parameter_1_part, self.function_name)=="neni":
            print("Nastaveni zustalo bezezmeny! Stavajici nastaveni:")    
        else:
            setattr(self, self.attribute, changer(self.parameter_1_part, self.function_name))
            print("Nove nastaveni:")
            
    def change_configuration(self, CODE):
        self.CODE = CODE

        self.function_part = self.CODE[0:2]
        self.parameter_1_part = self.CODE[2:6]

        try:
            self.function_name = self.orders_dict[self.function_part]
            self.attribute = self.attribute_dict[self.function_name]
        except KeyError:
            print("neexistujici trida prikazu! Zkus to prosim znovu")
            self.err=True

    def parameters(self):
        i=1
        n=len(self.orders_dict)
        while i < n+1:
            atribut=str(self.attribute_dict[self.orders_dict["0"+str(i)]])
            print(atribut + " = " + str(getattr(self, atribut)))
            i+=1
        pass
        

        



