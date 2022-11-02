
from .gmodule.operator import Operator

class GenesConfig:

    def __init__(self,
                 genes_set: list[str],
                 start_generation_quantity: int,
                 genotype_length: int,
                 operators: list[Operator]
                 ) -> None:
        self.genes_set: list[str] = genes_set
        self.start_eneration_quantity: int = start_generation_quantity
        self.genotype_length: int = genotype_length
        self.operators: list[Operator] = operators

