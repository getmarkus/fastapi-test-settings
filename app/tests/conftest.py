from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest

from app.config import get_settings
from app.factory import create_app

dotenv_path = Path(".env.testing")
load_dotenv(dotenv_path=dotenv_path, override=True)

settings = get_settings()


@pytest.fixture(name="app")
def test_app():
    """Create test app instance only during test execution."""
    return create_app()


@pytest.fixture(name="client")
def client_fixture(app: FastAPI):
    with TestClient(app) as client:
        yield client
