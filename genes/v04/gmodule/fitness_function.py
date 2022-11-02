
from abc import ABC, abstractmethod
from .genotype import Genotype

class FitnessFunction(ABC):

    @abstractmethod
    def fit(self, genotype: Genotype) -> float:
        pass

