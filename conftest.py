import os
import pytest

BASE_URL = os.getenv("BASE_URL", "https://devorycloud.com")
API_URL = os.getenv("API_URL", "https://api.devorycloud.com")
DEVORY_EMAIL = os.getenv("DEVORY_EMAIL", "")
DEVORY_PASSWORD = os.getenv("DEVORY_PASSWORD", "")

PROTECTED_PATHS = [
    "/dashboard",
    "/dashboard/projects",
    "/dashboard/projects/new",
    "/dashboard/deployments",
    "/dashboard/usage",
    "/dashboard/billing",
    "/dashboard/github",
]


@pytest.fixture(scope="session")
def base_url():
    """pytest-playwright uses this base URL for page.goto('/')."""
    return BASE_URL
