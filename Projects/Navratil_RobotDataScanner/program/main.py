import pandas as pd

import sys
from pathlib import Path

sys.path.insert(0, Path(__file__).parent.as_posix())

from robot import robot


if __name__ == "__main__":

    while True:

        # TODO programatic input
        # Bud zada uzivatel nebo jako parametr
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
            # print("To by mohlo jit")
            robot.change_configuration(scan)

            robot.run()

            # Print result from where its stored
            result = getattr(robot, robot.attribute)
            print(result)

    print("Program byl uspesne ukoncen")
