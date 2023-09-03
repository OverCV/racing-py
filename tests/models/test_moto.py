import pytest
from app.models.moto import Moto


@pytest.fixture
def moto_instance():
    moto = Moto(10, 11, 4, 100, 5)
    yield moto


@pytest.mark.parametrize(
    'expected', [
        (1)
    ])
def test_capacidad(expected, moto_instance):
    assert moto_instance.capacidad() == expected


@pytest.mark.parametrize(
    'expected', [
        (True, True, True, True, False)
    ])
def test_cambio(expected, moto_instance):
    for expect in expected:
        assert moto_instance.cambio() is expect
