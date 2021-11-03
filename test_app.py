from app import *
#ds

# websitePath = https://rh-to-do-list.herokuapp.com

# websitePath = http://127.0.0.1:5000


def test_index():
    
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200