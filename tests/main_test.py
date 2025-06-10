import pytest
import src.main

@pytest.fixture
def client():
    main.app.testing = True
    return main.app.test_client()

def test_hello_world(client):
    """Test the hello world endpoint."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b"Hello, World!"
