from app import *

# ds

# websitePath = https://rh-to-do-list.herokuapp.com

# websitePath = http://127.0.0.1:5000


def test_index():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_add():
    client = app.test_client()
    response = client.get("/")
    webpage_text = response.get_data()
    url = "/add"
    newTask = {"task": "test"}
    response = client.post(url, data=newTask)
    assert response.status_code == 302
    response = client.get("/")
    webpage_text = response.get_data()
    assert b"test" in webpage_text


def test_remove():
    # add task
    client = app.test_client()
    response = client.get("/")
    webpage_text = response.get_data()
    url = "/add"
    newTask = {"task": "test"}
    response = client.post(url, data=newTask)
    assert response.status_code == 302
    response = client.get("/")
    webpage_text = response.get_data()
    assert b"test" in webpage_text

    # test remove
    url = "/remove/test"
    response = client.get(url)
    webpage_text = response.get_data()
    assert b"test" not in webpage_text


def test_addTag():
    # add task
    client = app.test_client()
    response = client.get("/")
    webpage_text = response.get_data()
    url = "/add"
    newTask = {"task": "test"}
    response = client.post(url, data=newTask)
    assert response.status_code == 302
    response = client.get("/")
    webpage_text = response.get_data()
    assert b"test" in webpage_text

    # add tag and test
    url = "/addTag/test"
    newTag = {"test": "testTag"}
    response = client.post(url, data=newTag)
    response = client.get("/")
    webpage_text = response.get_data()
    assert b"testTag" in webpage_text
