from functools import reduce


class HigherOrderFunctions:
    """Examples of all higher order functions."""
    def __init__(self):
        """Initiates a list and dict input."""
        self.list = list(range(1, 11))
        self.dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 10: "ten"}

    def map_result(self):
        print('Example of map function.')
        return list(map(lambda x: x ** 3, self.list))

    def filter_result(self):
        print('Example of filter function.')
        return list(filter(lambda x: x % 3 == 0, self.list))

    def reduce_result(self):
        print('Example of reduce function.')
        return ''.join((reduce(lambda x, y: str(x) + str(y), self.list)))

    def even_filter(self):
        print('Example of filtering even numbers from a dictionary values.')
        return [value for key, value in self.dict.items() if key % 2 == 0]

    def list_comprehension(self):
        print('Examples of list comprehension.')
        print([x ** 3 for x in self.list])
        print([x for x in self.list if x % 3 == 0])
        print([x ** 3 for x in self.list if x % 3 == 0])


if __name__ == '__main__':
    print(HigherOrderFunctions().map_result(), '\n')
    print(HigherOrderFunctions().filter_result(), '\n')
    print(HigherOrderFunctions().reduce_result(), '\n')
    print(HigherOrderFunctions().even_filter(), '\n')
    HigherOrderFunctions().list_comprehension()
