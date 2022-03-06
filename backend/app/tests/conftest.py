import pytest
from faker import Faker
from starlette.testclient import TestClient

from app.api.deps import get_db
from app.db.session import Base
from app.main import app
from app.tests.database import TestingSessionLocal
from app.tests.database import engine as test_engine


@pytest.fixture()
def db():
    Base.metadata.create_all(bind=test_engine)
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        Base.metadata.drop_all(bind=test_engine)
        db.close()


@pytest.fixture()
def client():
    app.dependency_overrides[get_db] = db
    client = TestClient(app)
    return client


@pytest.fixture()
def fake():
    return Faker()
