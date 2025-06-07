import pytest
from app import create_flask_app

@pytest.fixture
def client():
    app = create_flask_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'html' in response.data.lower()

def test_main_route(client):
    response = client.get('/main')
    assert response.status_code == 200
    assert b'html' in response.data.lower()

def test_about_route(client):
    response = client.get('/about')
    assert response.status_code == 200
    assert b'html' in response.data.lower()

def test_upload_no_file(client):
    response = client.post('/upload', data={})
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'error' in json_data
    assert json_data['error'] == 'No file part'

def test_upload_empty_file(client):
    data = {
        'file': (b'', '')
    }
    response = client.post('/upload', data=data)
    assert response.status_code == 200
    json_data = response.get_json()
    assert 'error' in json_data
    assert json_data['error'] == 'No selected file'
