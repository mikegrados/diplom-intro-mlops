#  1) Malas practicas: multiples funciones con pruebas
#  2) Buenas practicas: pruebas parametrizadas
#  3) Marks: colocas skip y failed

from calculadora.app.operaciones import obtener_fracciones

# 1) Malas practicas
def test_obtener_fracciones():
    assert obtener_fracciones("10") == 10


def test_obtener_fracciones_2():
    assert obtener_fracciones("7/4") == 1.75


def test_obtener_fracciones_3():
    assert obtener_fracciones("-1") == -1


# 2) Buenas practicas
import pytest


def obtener_datos_test_obtener_fracciones():
    return [(10, 10), ("7/4", 1.75), (-1, -1)]


@pytest.mark.parametrize("num1, esperado", obtener_datos_test_obtener_fracciones())
def test_obtener_fracciones_parametrize(num1, esperado):
    assert obtener_fracciones(num1) == esperado


# 3) Marks
#   skip
@pytest.mark.skip(reason="No hay forma de probar esto ahora")
def test_convertir_binario():
    ...


#   xfail
@pytest.mark.xfail
def test_obtener_fracciones_falla():
    assert obtener_fracciones("diez") == "diez"


#   Escribir una marca personal
@pytest.mark.mi_marca
def test_obtener_fracciones_mi_marca():
    assert obtener_fracciones("2/4") == 0.5
