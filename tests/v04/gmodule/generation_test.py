import pytest

from genes.v04.factories.generation_factory import generation_factory
from genes.v04.gmodule.generation import Generation
from genes.v04.gmodule.individual import Individual
from genes.v04.gmodule.fitness_function import FitnessFunction


GENE_SET = ['0', '1']
GENOTYPE_LENGTH = 10
GENERATION_SIZE = 5
FITNESS_RESULT = 0.6


@pytest.fixture
def generation() -> Generation:
    return generation_factory(GENE_SET, GENOTYPE_LENGTH, GENERATION_SIZE)


@pytest.fixture
def fitness_function() ->FitnessFunction:
    return type(
        "SimpleFitnessFunction",
        (FitnessFunction, object),
        {
            "fit": lambda self, genotype: FITNESS_RESULT
        }
    )()


def test_create(generation: Generation) -> None:
    assert isinstance(generation, Generation)
    assert generation.size() == GENERATION_SIZE


def test_iterator(generation: Generation) -> None:
    for individual in generation:
        assert isinstance(individual, Individual)
        assert individual.fitness == 0.0
        assert individual.genotype.length() == GENOTYPE_LENGTH


def test_fitness(generation: Generation, fitness_function: FitnessFunction) -> None:
    generation.fit(fitness_function)
    for individual in generation:
        assert individual.fitness == FITNESS_RESULT

