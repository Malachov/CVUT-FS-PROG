import mypythontools

# Find paths and add to sys.path to be able to import local modules
mypythontools.tests.setup_tests()

from conftest import my_app


def test_1():
    my_app.test_function()
    assert True
