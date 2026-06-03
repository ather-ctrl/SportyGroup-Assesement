import pytest
from api.brewery_api import BreweryAPI


@pytest.fixture(scope="session")
def brewery_api():
    return BreweryAPI()