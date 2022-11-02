
from ..operator import Operator
from .crossover_method import CrossoverMethod
from ..generation import Generation


class Crossover(Operator):

    def __init__(self,
                 method: CrossoverMethod,
                 generation_size: int,
                 children_quantity: int,
                 ) -> None:
        self.generation_size: int = generation_size
        self.childern_quantity: int = childern_quantity
        self._method: CrossoverMethod = method

    def do(self, generation: Generation) -> Generation:
        next_generation = Generation()
        iteration: int = 0
        while next_generation.size() < self.generation_size:
            try:
                parents = self._method.choose_parents(iteration, generation)
            except IndexError:
                break

            for _ in range(0, self.childern_quantity):
                next_generation.add(self._method.child(parents))

            iteration += 1
        return next_generation

