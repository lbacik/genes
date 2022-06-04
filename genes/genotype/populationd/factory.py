from random import randint
from typing import List

from ..creature import Creature
from ..phenotype import Phenotype
from ..population import Population


def generate_phenotype(length: int, percentage: int = 50) -> Phenotype:
    phenotype: List[bool] = []
    for i in range(1, length):
        phenotype.append(True if randint(1, 101) <= percentage else False)
    return Phenotype(phenotype)


def create_population(number: int, length: int, percentage: int = 50) -> Population:
    population: Population = Population([])

    for i in range(0, number):
        phenotype: Phenotype = generate_phenotype(length, percentage)
        population.add(Creature(phenotype))

    return population
