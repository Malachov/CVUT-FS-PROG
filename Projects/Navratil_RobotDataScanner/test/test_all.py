import mypythontools
import pytest
import pandas
mypythontools.tests.setup_tests()

import funkce
from robot import Robot
# testdata1=(
#         ("0002", "gripper_change", "drill")
#         ("0001", "recording", False)
#         ("9999", "recording", "neni")
# )
# @pytest.mark.parametrize("a,b,expected", testdata1)
# def test_changer(a, b, expected):
#     # TODO
#     nacteno = funkce.changer(a, b)
#     assert nacteno == expected

def test_changer():
    assert funkce.changer("0002", "gripper_change") == "drill"
    assert funkce.changer("0001", "recording") == True
    assert funkce.changer("9999", "recording") == "neni"


def test_check_function_return_is_in_attribute():
    # TODO
    # Zavolat robota s kodem
    robot = Robot()
    robot.change_configuration("030003")
    robot.run()
    assert robot.gripper == "screwdriver"
    pass

