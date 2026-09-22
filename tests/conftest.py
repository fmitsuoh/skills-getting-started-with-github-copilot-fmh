import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    # Prevents signup/unregister mutations from leaking into other tests
    original_state = copy.deepcopy(activities)
    yield
    activities.clear()
    activities.update(original_state)
