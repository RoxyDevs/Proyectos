import pytest
from backend.app import app, db
from backend.models import SensorData
from datetime import datetime, timezone

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    client = app.test_client()

    with app.app_context():
        db.create_all()

    yield client

    with app.app_context():
        db.drop_all()

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200

def test_historical_route(client):
    response = client.get('/historical?start_date=2023-10-01&end_date=2023-10-31')
    assert response.status_code == 200