import pytest
from typing import Tuple
from genes.genotype.genotype import Genotype
from genes.genotype.genotyped.error.genotype_factory_error import GenotypeFactoryError
from genes.genotype.genotyped.factory import Factory as GenotypeFactory


def genotypes_to_create() -> Tuple:
    data = [
        ('',),
        ('0',),
        ('1',),
        ('00000000',),
        ('10101010001111010001101000101111100101010101010100001110001010001',),
    ]
    for row in data:
        yield row


def wrong_genotypes() -> Tuple:
    data = [
        (' ',),
        ('a',),
        ('0110 ',),
        ('11x',),
    ]
    for row in data:
        yield row


@pytest.mark.parametrize(['genotype_as_string'], genotypes_to_create())
def test_genotype_from_string_creation(genotype_as_string: str):
    genotype = GenotypeFactory.create_from_string(genotype_as_string)
    assert isinstance(genotype, Genotype)
    assert len(genotype_as_string) == len(genotype._data)


@pytest.mark.parametrize(['genotype_as_string'], wrong_genotypes())
def test_genotype_from_string_error(genotype_as_string: str):
    with pytest.raises(GenotypeFactoryError):
        GenotypeFactory.create_from_string(genotype_as_string)
