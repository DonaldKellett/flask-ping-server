import json

def test_ping(client):
    response = client.get('/ping/')
    assert response.content_type == 'application/json'
    body = json.loads(response.data)
    assert 'message' in body
    assert body['message'] == 'pong'

def test_app_version(client):
    response = client.get('/version/')
    assert response.content_type == 'application/json'
    body = json.loads(response.data)
    assert 'version' in body
    assert body['version'] == '0.0.1'
