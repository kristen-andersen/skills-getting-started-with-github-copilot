from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture(scope="function")
def client():
    baseline_activities = deepcopy(activities)
    with TestClient(app) as test_client:
        yield test_client

    activities.clear()
    activities.update(deepcopy(baseline_activities))
