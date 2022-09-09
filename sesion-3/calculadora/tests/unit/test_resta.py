#  1) Malas practicas: multiples funciones con pruebas
#  2) Buenas practicas: pruebas parametrizadas
#  3) Marks: colocas skip y failed

from calculadora.app.operaciones import resta

# 1) Malas practicas
def test_resta():
    assert resta("0.5", "0.5") == 0


def test_resta_2():
    assert resta("1/2", "1") == -0.5


def test_resta_3():
    assert resta("10", "5") == 5


# 2) Buenas practicas
import pytest


def obtener_datos_test_resta():
    return [(0.5, 0.5, 0), ("1/2", "1", -0.5), (10, "5", 5)]


@pytest.mark.parametrize("num1, num2, esperado", obtener_datos_test_resta())
def test_resta_parametrize(num1, num2, esperado):
    assert resta(num1, num2) == esperado


# 3) Marks
#   skip
@pytest.mark.skip(reason="No hay forma de probar esto ahora")
def test_resta_imaginarios():
    ...


#   xfail
@pytest.mark.xfail
def test_resta_falla():
    assert resta("2", "2") == 5


#   Escribir una marca personal
@pytest.mark.mi_marca
def test_resta_mi_marca():
    assert resta("8", "2") == 6
