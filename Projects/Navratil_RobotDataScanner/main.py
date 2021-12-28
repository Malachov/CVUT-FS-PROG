import sys
from pathlib import Path
import logging
from funkce import recording

sys.path.insert(0, Path(__file__).parent.as_posix())

from robot import Robot

logging.basicConfig(filename="logs.txt", level=logging.DEBUG, format="%(asctime)s %(levelname)s: %(message)s")


#if __name__ == "__main__":
def proces():
    logging.info("SPUSTEN program")
    print("-------------------------------\nSPUSTEN PROGRAM OVLADANI ROBOTA\n-------------------------------")
    print("nacteno zakladni nastaveni:\n")
    robot = Robot()

    print("\nZmenu parametru lze provest zadanim sestimistneho kodu pro vykonani prikazu\nUkonceni programu se provede zadanim kodu 000000")
    print("Zobrazeni vsech aktualnich nastaveni se zobrazi kodem 999999")

    while True:

        # TODO programatic input
        # Bud zada uzivatel nebo jako parametr
        scan = input("Zadej novy PRIKAZ:\n")
        logging.debug(scan)
        if scan == "000000":
            Konec = input("Nacten ukoncovaci kod. Program se nyni ukonci: (Y/N)")
            if Konec == "Y" or Konec == "y":
                print("Zvoleno ukonceni programu, nashledanou")
                break
            else:
                print("Program dale pokracuje")
        elif scan == "999999":
            print("Soucasne nastaveni robota:")
            robot.parameters

        elif len(scan) != 6:
            print("Spatny format cisla!")
            logging.warning("NumberFormatError")
        else:
            # print("To by mohlo jit")
            robot.change_configuration(scan)

            robot.run()

            # Print result from where its stored
            try:
                result = str(getattr(robot, robot.attribute))
                print(robot.attribute + " = " + result)
                if robot.recording == True or robot.attribute == "recording":
                    logging.info("%s = %s",robot.attribute, result)
                
            except AttributeError:
                print("Robot zustal bezezmeny!")
                logging.warning("AttributeError")

    print("Program byl uspesne ukoncen\n---------------------------")
    logging.info("UKONCEN program\n---------------")
