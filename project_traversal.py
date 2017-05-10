import os
from pprint import pprint


global PREFIX
PREFIX = "../../"


def validate_input_dir(directory):
    """
    This function checks if the given Directory exists.
    :param directory: a directory (path form)
    :return: True if the directory exists, False otherwise.
    """
    if os.path.exists(directory):
        return True
    return False


def tokenize(directory):
    """
    This function gets a path to a directory and it breaks it
    into prefix and neat directory name. For example, assume we
    have this path /home/user/Desktop this function with break it
    into a prefix = /home/user/ and a directory name Desktop.
    :param directory: The given Directory
    :return: the prefix and the name
    """
    dir_name = ""
    prefix = ""
    token = False
    for char in directory[-1::-1]:
        if char == "/" or char == "\\":
            token = True
        if token:
            prefix += char
        else:
            dir_name += char
    return dir_name[-1::-1], prefix[-1::-1]


def index_parent(directory):
    """
    This function lists all the contents of a given directory (eg. files, subdirectories).
    Furthermore, this function classifies the content of the specifies directory
    into file list and subdirectory list.
    :param directory: The directory we are indexing
    :return: the classification of the contents in separate lists
    """
    subdirectories = []
    files = []
    print(os.getcwd())
    for content in os.listdir(PREFIX + directory):
        if os.path.isdir(PREFIX + directory + "/" + content):
            subdirectories.append(content)
        else:
            files.append(content)
    pprint(subdirectories)
    pprint(files)
    return subdirectories, files

if __name__ == '__main__':
    subs, files = index_parent('Desktop')
    print(tokenize("../../Desktop"))
