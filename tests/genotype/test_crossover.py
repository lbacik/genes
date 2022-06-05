import pytest

from genes.genotype.creature import Creature
from genes.genotype.operatord.crossover import Crossover
from genes.genotype.operatord.selection import Selection
from genes.genotype.genotype import Genotype
from genes.genotype.population import Population


@pytest.fixture
def population():
    result = Population([])
    result.add(Creature(Genotype([False, False])))
    result.add(Creature(Genotype([True, True])))
    result.add(Creature(Genotype([False, False])))
    return result


def test_crossover(population):
    crossover = Crossover({
        Crossover.POPULATION_SIZE: 1,
        Crossover.CHILDREN_PER_PARENTS: 1,
    })
    result = crossover.do(population)

    assert result.size() == 1
    assert result._population[0].genotype()._data == [False, True]


def test_crossover_multi(population):
    crossover = Crossover({
        Crossover.POPULATION_SIZE: 2,
        Crossover.CHILDREN_PER_PARENTS: 2,
    })
    result = crossover.do(population)

    assert result.size() == 2
    assert result._population[0].genotype()._data == [False, True]
    assert result._population[1].genotype()._data == [False, True]


def test_crossover_poly(population):
    crossover = Crossover({
        Crossover.POPULATION_SIZE: 2,
        Crossover.CHILDREN_PER_PARENTS: 1,
        Crossover.CROSSOVER_TYPE: Crossover.CROSSOVER_TYPE_POLY,
    })
    result = crossover.do(population)

    assert result.size() == 2
    assert result._population[0].genotype()._data == [False, True]
    assert result._population[1].genotype()._data == [False, False]
