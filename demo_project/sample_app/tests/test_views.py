
# for the record, I don't like to use the Django Test Client
# This is just for demonstration purposes
from django.test import Client

def test_request():
    client = Client()
    response = client.get('/index')
    assert response.status_code == 200