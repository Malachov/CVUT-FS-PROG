import sys
from pathlib import Path

sys.path.insert(0, Path(__file__).parent.as_posix())

from robot import Robot



#if __name__ == "__main__":
def proces():
    print("SPUSTEN PROGRAM OVLADANI ROBOTA \n\nnacteno zakladni nastaveni:\n")
    
    robot = Robot()

    print("\nZmenu parametru lze provest zadanim sestimistneho kodu pro vykonani prikazu\nUkonceni programu se provede zadanim kodu 000000")

    while True:

        # TODO programatic input
        # Bud zada uzivatel nebo jako parametr
        scan = input("Zadej novy PRIKAZ:\n")

        if scan == "000000":
            Konec = input("Nacten ukoncovaci kod. Program se nyni ukonci: (Y/N)")
            if Konec == "Y" or Konec == "y":
                print("Zvoleno ukonceni programu, nashledanou")
                break
            else:
                print("Program dale pokracuje")
        elif scan == "999999":
            robot.parameters()
        elif len(scan) != 6:
            print("Spatny format cisla!")
        else:
            # print("To by mohlo jit")
            robot.change_configuration(scan)

            robot.run()

            # Print result from where its stored
            try:
                result = str(getattr(robot, robot.attribute))
                print(robot.attribute + " = " + result)
            except AttributeError:
                print("Robot zustal bezezmeny!")

    print("Program byl uspesne ukoncen")

