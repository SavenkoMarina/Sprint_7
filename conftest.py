import pytest
from api.scooter_api import CourierAPI, OrderAPI
from helpers import register_new_courier_and_return_login_password

@pytest.fixture
def courier_api():
    return CourierAPI()

@pytest.fixture
def order_api():
    return OrderAPI()

@pytest.fixture
def courier(courier_api):
    courier, _ = register_new_courier_and_return_login_password()
    yield courier
    response = courier_api.login(courier[0], courier[1])
    courier_id = response.json()["id"]

