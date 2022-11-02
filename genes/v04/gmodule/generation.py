
from .individual import Individual
from .fitness_function import FitnessFunction

class Generation:

    _index: int

    def __init__(self) -> None:
        self.individuals: list[Individual] = []

    def add(self, individual: Individual) -> None:
        self.individuals.append(individual)

    def fit(self, fitness_function: FitnessFunction) -> None:
        for individual in self.individuals:
            individual.fit(fitness_function)

    def size(self) -> int:
        return len(self.individuals)

    def sort_by_fitness(self) -> None:
        self.individuals.sort(key=lambda item: item.fitness, reverse=True)

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self) -> Individual:
        result: Individual
        try:
            result = self.individuals[self._index]
            self._index += 1
        except IndexError:
            raise StopIteration
        return result

