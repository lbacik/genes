
from ..gmodule.generation import Generation


class GenerationStatistics:

    FIT_MIN = 'min'
    FIT_MAX = 'max'
    FIT_AVR = 'avr'
    POPULATION_INDIVIDUALS = 'individuals'

    def __init__(self) -> None:
        self.data: list = []

    def add(self, generation: Generation) -> None:
        record: dict = {}
        fit_min = fit_max = None
        hashes: set = set()
        fit_sum = 0

        for individual in generation:
            if fit_min is None or individual.fitness < fit_min:
                fit_min = individual.fitness
            if fit_max is None or individual.fitness > fit_max:
                fit_max = individual.fitness
            fit_sum += individual.fitness
            hashes.add(hash(individual.genotype.__str__()))

        record[self.FIT_MIN] = fit_min
        record[self.FIT_MAX] = fit_max
        record[self.FIT_AVR] = fit_sum / generation.size()
        record[self.POPULATION_INDIVIDUALS] = len(hashes)

        self.data.append(record)

