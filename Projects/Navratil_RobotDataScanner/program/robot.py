# TODO ukol
#
# - 1) podle ostatnich cisel vlozit parametry do funkce
# - 2) Vytvorit objekt robota z skriptu main a zavolat prislusnou funci s parametry


def func_scanner_change():
    # Connect OPC server - run login
    print("it works")
    pass


def ref_point_change():
    # Connect OPC server - run login
    print("it also works")
    pass


class Robot:
    def __init__(self, CODE="Default") -> None:
        self.CODE = CODE

        self.function_part = self.CODE[0:2]
        self.parameter_1_part = self.CODE[2:4]

        function_name = self.orders_dict[self.function_part]
        self.used_function = self.function_dict[function_name]

    orders_dict = {
        "01": "scanner_change",
        "02": "ref_point_change",
        "03": "gripper_change",
        "04": "speed_change",
    }

    function_dict = {
        "scanner_change": func_scanner_change,
        "ref_point_change": ref_point_change,
        "gripper_change": func_scanner_change,
        "speed_change": func_scanner_change,
    }

    def run(self):
        self.used_function()


robot_orders = Robot("0202135")
robot_orders_2 = Robot("02")


robot_orders.run()


a = 8
