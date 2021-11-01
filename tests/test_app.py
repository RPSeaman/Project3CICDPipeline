import sys
sys.path.insert(0, '../src')
from app import index


def test_index():
    assert index() == "hello, world!"
 