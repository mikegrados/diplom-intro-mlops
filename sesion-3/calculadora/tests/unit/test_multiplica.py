#  1) Malas practicas: multiples funciones con pruebas
#  2) Buenas practicas: pruebas parametrizadas
#  3) Marks: colocas skip y failed

from calculadora.app.operaciones import multiplica

# 1) Malas practicas
def test_multiplica():
    assert multiplica("-2", "3") == -6


def test_multiplica_2():
    assert multiplica("1/2", "8/4") == 1


def test_multiplica_3():
    assert multiplica("10", "5") == 50


# 2) Buenas practicas
import pytest


def obtener_datos_test_multiplica():
    return [(-2, 3, -6), ("1/2", "8/4", 1), (10, "5", 50)]


@pytest.mark.parametrize("num1, num2, esperado", obtener_datos_test_multiplica())
def test_multiplica_parametrize(num1, num2, esperado):
    assert multiplica(num1, num2) == esperado


# 3) Marks
#   skip
@pytest.mark.skip(reason="No hay forma de probar esto ahora")
def test_multiplica_imaginarios():
    ...


#   xfail
@pytest.mark.xfail
def test_multiplica_falla():
    assert multiplica("4i", "2") == "pez"


#   Escribir una marca personal
@pytest.mark.mi_marca
def test_multiplica_mi_marca():
    assert multiplica("8", "2") == 16
