

class Genotype:

    def __init__(self, genes: list[str]) -> None:
        self.genes: list[str] = genes
        self.str_separator = ''

    def length(self) -> int:
        return len(self.genes)

    def __getitem__(self, item: int) -> str:
        return self.genes[item]

    def __str__(self) -> str:
        return self.str_separator.join(self.genes)

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self) -> str:
        try:
            result = self.genes[self._index]
            self._index += 1
        except IndexError:
            raise StopIteration
        return result

