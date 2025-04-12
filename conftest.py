import pytest
from api.scooter_api import CourierAPI, OrderAPI

@pytest.fixture
def courier_api():
    return CourierAPI()

@pytest.fixture
def order_api():
    return OrderAPI()
