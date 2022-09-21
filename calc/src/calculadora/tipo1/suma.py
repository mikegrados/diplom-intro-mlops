from calculadora.utils.fraccion import obtener_fracciones


def suma(a, b):
    sumando_a = obtener_fracciones(a)
    sumando_b = obtener_fracciones(b)
    return sumando_a + sumando_b
