import sys
from pprint import pprint


def classify(module):
    print(module)
    print(module in sys.builtin_module_names)
    print(module in sys.modules)

    if module in sys.builtin_module_names:
        return "built-in"
    elif module in sys.modules:
        return "standard library"
    else:
        return "third-party"

if __name__ == '__main__':
    type = classify("numpy")
    print(type)
    #pprint(sys.modules)