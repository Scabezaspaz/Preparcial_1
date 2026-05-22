import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'src'))
from registro_notas import RegistroNotas

@pytest.fixture
def registro():
    return RegistroNotas()