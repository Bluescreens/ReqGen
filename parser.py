import re
from pprint import pprint


class PythonParser:
    def __init__(self, indexes):
        self.indexes = {}
        self.indexes = indexes
        self.project_requirements = set()

    @staticmethod
    def clear_list(ls):
        if "import" in ls:
            ls.remove("import")
        return ls

    def parse_file(self, file):
        with open(file) as script:
            print(file)
            for line in script:
                #print(line)
                pattern = re.match(r"from\s(\S*)\simport\s(.*)", line)
                if re.match(r"import\s", line):
                    modules = re.findall(r'[^,\s]+', line)
                    modules = self.clear_list(modules)
                    self.add_requirement(modules)
                if pattern:
                    self.add_requirement(pattern.group(1))

    def add_requirement(self, requirement):
        if isinstance(requirement, list):
            for _ in requirement:
                self.project_requirements.add(_)
        else:
            self.project_requirements.add(requirement)

    def recreate_file(self, key, value):
        return key + value

    def mass_parsing(self):
        for directory, file_lists in self.indexes.items():
            if len(file_lists) == 0:
                continue
            for file in file_lists:
                file_name = self.recreate_file(directory, file)
                self.parse_file(file_name)
        self.display_results()

    def display_results(self):
        pprint(self.project_requirements)
