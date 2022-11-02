from abc import ABC, abstractmethod
from random import randint
from ..generation import Generation
from ..individual import Individual
from ..genotype import Genotype


class CrossoverMethod(ABC):

    @abstractmethod
    def choose_parents(
            self,
            iteration: int,
            generation: Generation
    ) -> tuple[Individual, Individual]:
        pass

    @staticmethod
    def child(parents: tuple[Individual, Individual]) -> Individual:
        cross_point: int = randint(1, parents[0].genotype.length() - 1)
        new_genotype = Genotype(
            parents[0].genotype.genes[0:cross_point]
            + parents[1].genotype.genes[cross_point:]
        )
        return Individual(new_genotype)

