from my_package.example import hello


def test_hello():
    """Example test with parametrization."""
    assert hello("Bob") == "Hello Bob!"
    assert hello("Alice") == "Hello Alice!"
