#  1) Malas practicas: multiples funciones con pruebas
#  2) Buenas practicas: pruebas parametrizadas
#  3) Marks: colocas skip y failed

from calculadora.app.operaciones import divide

# 1) Malas practicas
def test_divide():
    assert divide("10", "2") == 5


def test_divide_2():
    assert divide("-15/4", "1/2") == -7.5


def test_divide_3():
    # assert divide("4", "3") == 1.3 # EDGE CASE por los numeros .3333333
    assert divide("8", "16") == 0.5


# 2) Buenas practicas
import pytest


def obtener_datos_test_divide():
    return [(10, 2, 5), ("-15/4", "1/2", -7.5), (8, "16", 0.5)]


@pytest.mark.parametrize("num1, num2, esperado", obtener_datos_test_divide())
def test_divide_parametrize(num1, num2, esperado):
    assert divide(num1, num2) == esperado


# 3) Marks
#   skip
@pytest.mark.skip(reason="No hay forma de probar esto ahora")
def test_divide_imaginarios():
    ...


#   xfail
@pytest.mark.xfail
def test_divide_falla():
    assert divide("7", "0") == "indeterminado"


#   Escribir una marca personal
@pytest.mark.mi_marca
def test_divide_mi_marca():
    assert divide("4", "2") == 2
