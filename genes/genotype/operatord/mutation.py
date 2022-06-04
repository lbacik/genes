import random

from ..creature import Creature
from ..operator import Operator
from ..population import Population


class Mutation(Operator):

    MUTATION_PROBABILITY = 'mutation_probability'

    _config: dict = {
        MUTATION_PROBABILITY: 0.5,
    }

    def __init__(self, config: dict = None):
        if config is not None:
            self._config = config

    def do(self, population: Population) -> Population:
        creature: Creature
        for creature in population:
            if random.random() < self._config[self.MUTATION_PROBABILITY]:
                index: int = random.randrange(0, len(creature.phenotype().data()))
                creature.phenotype().data()[index] = not creature.phenotype().data()[index]
        return population
