import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import src.main import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_hello_world(client):
    """Test the hello world endpoint."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b"Hello, World!"
