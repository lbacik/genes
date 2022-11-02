import random

from ..operator import Operator
from ..generation import Generation
from ..genotype import Genotype


class Mutation(Operator):

    def __init__(self,
                 gene_set: list[str],
                 probability: float,
                 ) -> None:
        self.probability: float = probability
        self.gene_set: list[str] = gene_set

    def do(self, generation: Generation) -> None:
        for individual in generation:
            if self._probability_met:
                self.mutate(individual.genotype)

    def mutate(self, genotype: Genotype) -> None:
        index: int = random.randrange(0, genotype.length())
        new_gene: str = self._get_new_gene(genotype.genes[index])
        genotype.genes[index] = new_gene

    def _probability_met(self) -> bool:
        return random.random() < self.probability

    def _get_new_gene(self, gene: str) -> str:
        first, second = random.sample(self.gene_set, 2)
        return second if first == gene else first

