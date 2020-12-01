from app import *
import pytest
@pytest.fixture
def app():
    return app
