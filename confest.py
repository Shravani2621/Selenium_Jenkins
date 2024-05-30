# conftest.py
import pytest

def pytest_configure(config):
    config.addinivalue_line(
        "markers", "login: mark test as requiring login"
    )