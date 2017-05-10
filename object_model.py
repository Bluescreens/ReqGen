import os
from pprint import pprint


class DirectoryTraversal:
    def __init__(self, directory):
        self.PREFIX, self.dir_name = self.tokenize(directory)
        self.PATH = self.PREFIX + self.dir_name + "/"
        # self.children = {}
        self.queue = []
        self.indexes = {}
        self.visited = []
        # checking if the seed directory exists.
        if self.validate_input_dir(directory):
            self.queue.append(directory)
        else:
            print("Wrong Directory")
            exit(-1)

    @staticmethod
    def validate_input_dir(directory):
        """
        This function checks if the given Directory exists.
        :param directory: a directory (path form)
        :return: True if the directory exists, False otherwise.
        """
        if os.path.exists(directory):
            return True
        return False

    @staticmethod
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

    def current_directory(self):
        if not self.is_queue_empty():
            current_dir = self.queue.pop() + "/"
            self.indexes[current_dir] = []
            return current_dir
        return -1

    def is_queue_empty(self):
        if len(self.queue) == 0:
            return True
        return False

    def filter(self, directory, file):
        if ".py" in file or ".pyw" in file:
            self.indexes[directory].append(file)

    def index_parent(self, directory):
        """
        This function lists all the contents of a given directory (eg. files, subdirectories).
        Furthermore, this function classifies the content of the specifies directory
        into file list and subdirectory list.
        :param directory: The directory we are indexing
        :return: the classification of the contents in separate lists
        """
        # prefix, dir_name = self.tokenize(directory)
        # subdirectories = []
        # files = []
        # print(os.getcwd())
        for content in os.listdir(directory):
            if os.path.isdir(directory + content):
                self.queue.append(directory + content)
                # subdirectories.append(content)
                # self.children[self.PATH].append(content)
            else:
                # self.indexes[directory].append(content)
                self.filter(directory, content)
        # pprint(subdirectories)
        # pprint(files)
        # return subdirectories, files

    def traversal(self):
        while not self.is_queue_empty():
            current = self.current_directory()
            self.index_parent(current)
            self.visited.append(current)
        #pprint(self.visited)
        pprint(self.indexes)

if __name__ == '__main__':
    project = DirectoryTraversal('/home/rottencrab/PycharmProjects/ReqGen')
    project.traversal()
