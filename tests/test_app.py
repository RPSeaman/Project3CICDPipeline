from '../src/app.py' import index


def test_index():
    assert index() == "hello, world!"
 