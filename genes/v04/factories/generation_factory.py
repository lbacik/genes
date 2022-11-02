
from ..gmodule.generation import Generation
from .genotype_factory import genotype_factory
from ..gmodule.individual import Individual
from ..gmodule.genotype import Genotype


def generation_factory(
        genes_set: list[str],
        genotype_length: int,
        generation_size: int,
    ) -> Generation:
    generation: Generation = Generation()
    for _ in range(0, generation_size):
        genotype: Genotype = genotype_factory(genes_set, genotype_length)
        generation.add(Individual(genotype))
    return generation

