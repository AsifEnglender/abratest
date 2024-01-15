from app import app
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_hello(client):
    response = client.get('/')
    assert response.data == b'abra'
