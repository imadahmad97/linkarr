import pytest
import shutil
import os
from tests.setup_test_env import SetupTestEnv
from tests.teardown_test_env import teardown_test_env
import logging

logger = logging.getLogger(__name__)


@pytest.fixture(scope="session", autouse=True)
def setup_and_teardown_test_env():
    """
    Fixture to set up and tear down the test environment.
    """
    SetupTestEnv()

    yield

    teardown_test_env()
