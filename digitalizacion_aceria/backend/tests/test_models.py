import pytest
from backend.models import SensorData, db
from backend.app import app
from datetime import datetime, timezone

@pytest.fixture
def app_context():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield
        db.drop_all()

def test_sensor_data_model(app_context):
    data = SensorData(value=100.0, timestamp=datetime.now(timezone.utc))
    db.session.add(data)
    db.session.commit()

    retrieved_data = SensorData.query.first()
    assert retrieved_data.value == 100.0