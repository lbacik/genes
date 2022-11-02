import pytest
import random

from genes.v04.factories.generation_factory import generation_factory
from genes.v04.gmodule.operators.selection import Selection
from genes.v04.gmodule.generation import Generation


GENE_SET = ['a', 'b']


@pytest.fixture
def generation() -> Generation:
    generation: Generation = generation_factory(GENE_SET, 1, 3)
    fitness_values = random.sample([0, 0.1, 0.3], k=3)
    for individual in generation:
        individual.fitness = fitness_values.pop()
    return generation


def test_empty_select(generation: Generation) -> None:
    selection = Selection({
        Selection.QUANTITY: 0,
    })
    result = selection.do(generation)
    assert result.size() == 0


def test_select(generation: Generation) -> None:
    selection = Selection({
        Selection.QUANTITY: 2,
    })
    result = selection.do(generation)

    assert result.size() == 2
    assert result.individuals[0].fitness == 0.3
    assert result.individuals[1].fitness == 0.1


def test_select_more(generation: Generation) -> None:
    selection = Selection({
        Selection.QUANTITY: generation.size() * 2,
    })
    result = selection.do(generation)

    assert result.size() == generation.size()

