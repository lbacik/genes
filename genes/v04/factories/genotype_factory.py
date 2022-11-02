
import random

from ..gmodule.genotype import Genotype


def genotype_factory(
        genes_set: list[str],
        genotype_length: int,
    ) -> Genotype:
    return Genotype(random.choices(genes_set, k=genotype_length))


def genotype_from_str(genotype: str, sep='') -> Genotype:
    genes: list[str]
    if sep == '':
        genes = list(genotype)
    else:
        genes = genotype.split(sep)
    genotype = Genotype(genes)
    if sep != '':
        genotype.str_separator = sep
    return genotype

