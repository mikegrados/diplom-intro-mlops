import pytest

from calculadora.app.operaciones import divide
from calculadora.app.operaciones import multiplica
from calculadora.app.operaciones import suma
from calculadora.app.operaciones import resta
from calculadora.app.operaciones import resta


def test_divide():
    assert (suma("5", "5") * resta("5/4", "3/4")) == 5
    # (5+5)*(1.25-0.75) = (10)*(0.5) = 5
    # (8+7/5)*(15-3/8) = (9.4)*(14.625) = 137.475


def obtener_datos_test_integracion():
    return [(5, 5, "5/4", "3/4", 5), (8, "7/5", 15, "3/8", 137.475)]


@pytest.mark.parametrize(
    "num1, num2, num3, num4, esperado", obtener_datos_test_integracion()
)
def test_divide_parametrize(num1, num2, num3, num4, esperado):
    assert (suma(num1, num2) * resta(num3, num4)) == esperado
