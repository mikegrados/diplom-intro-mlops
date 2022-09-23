#  1) Malas practicas: multiples funciones con pruebas
#  2) Buenas practicas: pruebas parametrizadas
#  3) Marks: colocas skip y failed

from calculadora import suma

# 1) Malas practicas
def test_suma():
    assert suma("0.5", "0.5") == 1


def test_suma_2():
    assert suma("-3", "-3") == -6


def test_suma_3():
    assert suma("4", "6") == 10


# 2) Buenas practicas
import pytest


def obtener_datos_test_suma():
    return [(0.5, 0.5, 1), (-3, -3, -6), (4, 6, 10)]


@pytest.mark.parametrize("num1, num2, esperado", obtener_datos_test_suma())
def test_suma_parametrize(num1, num2, esperado):
    assert suma(num1, num2) == esperado


# 3) Marks
#   skip
@pytest.mark.skip(reason="No hay forma de probar esto ahora")
def test_raiz_cuadrada():
    ...


#   xfail
@pytest.mark.xfail
def test_suma_falla():
    assert suma("2", "2") == 5


#   Escribir una marca personal
@pytest.mark.mi_marca
def test_suma_mi_marca():
    assert suma("2", "2") == 4
