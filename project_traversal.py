import os
from pprint import pprint


global PREFIX
PREFIX = "../../"


def validate_input_dir(directory):
    if os.path.exists(directory):
        return True
    return False


def tokenize(directory):
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
