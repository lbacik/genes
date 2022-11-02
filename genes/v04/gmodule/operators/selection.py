
from ..operator import Operator
from ..generation import Generation


class Selection(Operator):

    def __init__(self,
                 quantity: int
                 ) -> None:
        self.quantity = quantity

    def do(self, generation: Generation) -> Generation:
        selection = Generation()

        generation.sort_by_fitness()

        for i in range(0, self.quantity):
            try:
                selection.add(generation.individuals[i])
            except IndexError:
                break

        return selection

