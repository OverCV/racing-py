import pytest
from app.models.moto import Moto


@pytest.fixture
def moto_instance():
    moto = Moto(11, 4, 100, 5)
    yield moto


@pytest.mark.parametrize(
    'expected', [
        (1)
    ])
def test_capacidad(expected, moto_instance):
    assert moto_instance.capacidad() == expected


@pytest.mark.parametrize(
    'expected', [
        (0)
    ])
def test_acelerar(expected, moto_instance):
    moto_instance.acelerar()
    assert moto_instance.dar_velocidad() == expected


@pytest.mark.parametrize(
    'expected', [
        (5)
    ])
def test_acelerar_cambio(expected, moto_instance):
    moto_instance.cambio()
    moto_instance.acelerar()
    assert moto_instance.dar_velocidad() == expected


@pytest.mark.parametrize(
    'expected', [
        # Can make 4 gear changes #
        (True, True, True, True, False)
    ])
def test_cambio(expected, moto_instance):
    for expect in expected:
        assert moto_instance.cambio() is expect
