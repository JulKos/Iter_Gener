# Итератор, который принимает список списков, и возвращает их плоское представление,
# т.е последовательность состоящую из вложенных элементов.


class FlatIterator:
    def __init__(self, nested_list):
        self.nested_list = sum(nested_list, [])

    def __iter__(self):
        self.cursor = - 1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.nested_list, ):
            raise StopIteration
        element = self.nested_list[self.cursor]
        return element


nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None]
]

for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)

# генератор, который принимает список списков, и возвращает их плоское представление


def flat_generator(nested_list):
    for el in sum(nested_list, []):
        yield el

for item in  flat_generator(nested_list):
	print(item)