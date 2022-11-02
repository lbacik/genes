
from .genotype import Genotype
from .fitness_function import FitnessFunction

class Individual:

    def __init__(self, genotype: Genotype, fitness: float = 0.0) -> None:
        self.fitness: float = fitness
        self.genotype: Genotype = genotype

    def fit(self, fitness_function: FitnessFunction) -> None:
        self.fitness = fitness_function.fit(self.genotype)

