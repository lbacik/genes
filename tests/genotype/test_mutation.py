import pytest

from genes.genotype.creature import Creature
from genes.genotype.operatord.mutation import Mutation
from genes.genotype.phenotype import Phenotype
from genes.genotype.population import Population


@pytest.fixture
def population():
    result = Population([])
    result.add(Creature(Phenotype([False])))
    return result


def test_mutation_0(population):
    mutation = Mutation({Mutation.MUTATION_PROBABILITY: 0})
    result = mutation.do(population)

    assert result.size() == 1
    assert result[0].phenotype()[0] is False


def test_mutation_100(population):
    mutation = Mutation({Mutation.MUTATION_PROBABILITY: 100})
    result = mutation.do(population)

    assert result.size() == 1
    assert result[0].phenotype()[0] is True
