import pytest

def pytest_addoption(parser):
    parser.addoption("--config-env")
    parser.addoption("--user-id")

@pytest.fixture
def config_env(request):
    return request.config.getoption("--config-env")

@pytest.fixture
def user_id(request):
    return request.config.getoption("--user-id")