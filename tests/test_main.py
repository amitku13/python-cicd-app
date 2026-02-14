from app.main import greet

def test_greet():
    assert greet("dev") == "Hello from dev environment!"