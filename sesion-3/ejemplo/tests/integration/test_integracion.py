import sys

sys.path.append("ejemplo/app")
sys.path.append("../")

import pytest

from ejemplo.app.funciones import procesar_nombre
from ejemplo.app.funciones import procesar_apellido_paterno
from ejemplo.app.funciones import procesar_apellido_materno


def concatenar_nombre_completo(nombre, ap, am):
    return nombre + " " + ap + " " + am


def obtener_datos_test_integracion():
    return [
        ("carlos", "LOPEZ", "meJIa", "Carlos Lopez Mejia"),
        ("ivan", "huERTA", "CoroNA", "Ivan Huerta Corona"),
    ]


@pytest.mark.parametrize("nombre, ap, am, esperado", obtener_datos_test_integracion())
def test_divide_parametrize(nombre, ap, am, esperado):
    assert (
        procesar_nombre(nombre)
        + " "
        + procesar_apellido_paterno(ap)
        + " "
        + procesar_apellido_materno(am)
        == esperado
    )
