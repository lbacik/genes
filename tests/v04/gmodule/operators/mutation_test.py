import pytest

from genes.v04.gmodule.operators.mutation import Mutation
from genes.v04.gmodule.generation import Generation
from genes.v04.factories.generation_factory import generation_factory


GENE_SET = ['a', 'b']


@pytest.fixture
def mutation() -> Mutation:
    return Mutation(GENE_SET, 1.0)


@pytest.fixture
def generation() -> Generation:
    return generation_factory(GENE_SET, genotype_length=1, generation_size=1)


def test_create(generation: Generation, mutation: Mutation) -> None:
    gene_before = generation.individuals[0].genotype[0]
    mutation.do(generation)
    gene_after = generation.individuals[0].genotype[0]
    assert gene_before != gene_after

