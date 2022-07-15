from datetime import datetime
import pytest


@pytest.fixture(scope='session', autouse=True)
def hello_and_bye():
    print('Starting...')
    print("Let's go!", datetime.now())
    yield
    print('Done', datetime.now())


@pytest.fixture
def current_time():
    return datetime.now()


def test_foo(current_time):
    print(current_time)


def test_bar(current_time):
    print(current_time)
