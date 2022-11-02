
from ..crossover_method import CrossoverMethod
from ...individual import Individual
from ...generation import Generation


class CrossoverMono(CrossoverMethod):

    def choose_parents(
            self,
            iteration: int,
            generation: Generation
    ) -> tuple[Individual, Individual]:

        parent1: Individual = generation.individuals[iteration * 2]
        parent2: Individual = generation.individuals[iteration * 2 + 1]
        return parent1, parent2
