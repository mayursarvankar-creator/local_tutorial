import pytest


@pytest.fixture(scope="session")
def app_url():
    return "https://ecommerce-playground.lambdatest.io"
