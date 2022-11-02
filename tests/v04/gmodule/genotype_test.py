import pytest

from genes.v04.gmodule.genotype import Genotype
from genes.v04.factories.genotype_factory import genotype_factory


GENOTYPE = ['0', '1', 'a', 'A', 'foo']


@pytest.fixture
def genotype() -> Genotype:
    genotype = Genotype(GENOTYPE)
    genotype.str_separator = ' '
    return genotype


def test_create(genotype: Genotype) -> None:
    assert isinstance(genotype, Genotype)
    assert genotype.__str__() == '0 1 a A foo'
    assert genotype.length() == len(GENOTYPE)


def test_iterator(genotype: Genotype) -> None:
    for index, value in enumerate(genotype):
        assert value == GENOTYPE[index]

def test_factory() -> None:
    genotype: Genotype = genotype_factory(['0', '1'], 1)
    assert isinstance(genotype, Genotype)
    assert genotype.length() == 1
    assert genotype.__str__() in {'0', '1'}

