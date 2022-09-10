import sys

sys.path.append("ejemplo/app")
sys.path.append("../")

import pytest

from ejemplo.app.funciones import procesar_nombre
from ejemplo.app.funciones import procesar_apellido_paterno
from ejemplo.app.funciones import procesar_apellido_materno

# Pruebas para el nombre
def obtener_datos_test_nombre():
    return [("carlos", "Carlos"), ("MiGuel", "Miguel"), ("iVAN", "Ivan")]


@pytest.mark.parametrize("nombre, esperado", obtener_datos_test_nombre())
def test_nombre_parametrize(nombre, esperado):
    assert procesar_nombre(nombre) == esperado


# Pruebas para el apellido paterno
def obtener_datos_test_ap():
    return [("LOPEZ", "Lopez"), ("EspiNOZA", "Espinoza"), ("sancHEz", "Sanchez")]


@pytest.mark.parametrize("ap, esperado", obtener_datos_test_ap())
def test_ap_parametrize(ap, esperado):
    assert procesar_apellido_paterno(ap) == esperado


# Pruebas para el apellido materno
def obtener_datos_test_am():
    return [("ferrer", "Ferrer"), ("SILVa", "Silva"), ("PalafoX", "Palafox")]


@pytest.mark.parametrize("am, esperado", obtener_datos_test_am())
def test_am_parametrize(am, esperado):
    assert procesar_apellido_materno(am) == esperado
