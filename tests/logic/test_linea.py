import pytest
from app.logic.linea import Linea


@pytest.fixture
def linea_instance():
    linea = Linea(500)
    yield linea


# @pytest.mark.parametrize(
#     'args, expected', [
#         ()
#     ])
# def test_locar_vehiculo(pos, expected, linea_instance):
#     assert linea_instance.locar_vehiculo(pos) == expected
