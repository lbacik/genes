from .genes_config import GenesConfig
from .gmodule.fitness_function import FitnessFunction
from .gmodule.generation import Generation
from .gmodule.operator import Operator
from .stats.generation_stats import GenerationStatistics


class Genes:
    def __init__(self,
        genes_config: GenesConfig,
        fitnes_function: FitnessFunction,
        start_generation: Generation,
        generation_stats: GenerationStatistics,
    ) -> None:
        self._genes_config: GenesConfig = genes_config
        self._fitnes_function: FitnessFunction = fitnes_function
        self.generation: Generation = start_generation
        self.generation_stats: GenerationStatistics = generation_stats
        self.generation_stats.add(self.generation)

    def next(self) -> None:
       self._execute_actions()
       self._fit_generation()
       self.generation_stats.add(self.generation)

    def _execute_actions(self) -> None:
        action: Operator
        for action in self._genes_config.operators:
            next_generation = action.do(self.generation)
            if isinstance(next_generation, Generation):
                self.generation: Generation = next_generation

    def _fit_generation(self) -> None:
        self.generation.fit(self._fitnes_function)

