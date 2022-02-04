from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

# test index route for 200 status


def test_index():
    response = client.get('/')
    assert response.status_code == 200


# test index route for message in response
def test_index_success_message():
    response = client.get('/')
    assert 'active' in response.json()['message']

# test add-user with payload for 200 status


def test_add_user():
    response = client.post('/add-user', json={
        "name": "test",
        "email": "buabajerry@gmail.com",
        "section": "test"
    })
    assert response.status_code == 200

# test add-user with existing user for 400 status


def test_add_user_with_existing_user():
    response = client.post('/add-user', json={
        "name": "test",
        "email": "buabajerrrry@gmail.com",
        "section": "test"
    })
    assert response.status_code == 400

# test add-user with missing payload for 400 status


def test_add_user_with_missing_payload():
    response = client.post('/add-user', json={
        "name": "",
        "email": "buabajerry@gmail.com",
        "section": "test"
    })
    assert response.status_code == 400

# test add-user with invalid request method for 405 status


def test_add_user_with_invalid_method():
    response = client.get('/add-user')
    assert response.status_code == 405

# test add-user route for message in response


def test_add_user_success_message():
    response = client.post('/add-user', json={
        "name": "test",
        "email": "buabajerry@gmail.com",
        "section": "test"
    })
    assert 'User added to database' in response.json()['message']
