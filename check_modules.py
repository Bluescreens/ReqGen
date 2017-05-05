import sys


def does_exist(module):
    """
    This function checks if a module exists
    in a specified environment.
    :param module: the module we want to check
    :return: The result of that search
    """
    if module in sys.modules:
        return True
    return False
