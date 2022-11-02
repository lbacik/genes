from ..crossover_method import CrossoverMethod
from ...individual import Individual
from ...generation import Generation


class CrossoverPoly(CrossoverMethod):

    def choose_parents(
            self,
            iteration: int,
            generation: Generation
    ) -> tuple[Individual, Individual]:

        parent1: Individual = generation.individuals[0]
        parent2: Individual = generation.individuals[iteration + 1]
        return parent1, parent2

