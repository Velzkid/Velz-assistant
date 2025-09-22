# tests/test_app.py

from src.utils import greet_user

def test_greet_user():
    assert greet_user("Tester") == "Hello, Tester! Welcome to Velz Assistant 🚀"
