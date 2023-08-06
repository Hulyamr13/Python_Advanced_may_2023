class Program:
    @staticmethod
    def main():
        input_strings = input().split(", ")
        target_string = input().strip()

        wc = WordCruncher(input_strings, target_string)

        for path in wc.get_paths():
            print(path)


class WordCruncher:
    def __init__(self, input_strings, target_string):
        self.results = set()
        self.permutation = self.generate_permutations(sorted(input_strings), target_string)

        for path in self.get_all_paths():
            result = ' '.join(path)
            if result not in self.results:
                self.results.add(result)

    def get_paths(self):
        return self.results

    def get_all_paths(self):
        way = []
        for key in self.visit_path(self.permutation, []):
            if key is None:
                yield way
                way = []
            else:
                way.append(key)

    @staticmethod
    def generate_permutations(input_strings, target_string):
        if not target_string or len(input_strings) == 0:
            return None

        return_values = []
        for i, key in enumerate(input_strings):
            if target_string.startswith(key):
                node = Node(key)
                node.value = WordCruncher.generate_permutations(input_strings[:i] + input_strings[i+1:], target_string[len(key):])

                if node.value is None and node.key != target_string:
                    continue

                return_values.append(node)

        return return_values

    @staticmethod
    def visit_path(permutation, path):
        if permutation is None:
            for path_item in path:
                yield path_item
            yield None
        else:
            for node in permutation:
                path.append(node.key)
                yield from WordCruncher.visit_path(node.value, path)
                path.pop()


class Node:
    def __init__(self, key):
        self.key = key
        self.value = None


if __name__ == '__main__':
    Program.main()
