from calculadora.utils import obtener_fracciones


def division(a, b):
    dividendo = obtener_fracciones(a)
    divisor = obtener_fracciones(b)
    try:
        return dividendo / divisor
    except ZeroDivisionError:
        return "Division entre cero"
