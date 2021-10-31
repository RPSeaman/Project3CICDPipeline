import '../src/app.py' as app


def test_index():
    assert app.index() == "hello, world!"
 