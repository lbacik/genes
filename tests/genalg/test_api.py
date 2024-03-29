
import pytest
from unittest import mock
from genes.genalg.api import GeneticAlgorithmApi
from genes.genalg.config import Config


@pytest.fixture()
def api():
    fitness_function = mock.Mock()
    return GeneticAlgorithmApi(
        None,
        Config(),
        fitness_function,
        []
    )


def test_api_instantiate(api):
    assert isinstance(api, GeneticAlgorithmApi)


def test_ng_without_init(api: GeneticAlgorithmApi):
    assert api.next_generation() == api.population()
