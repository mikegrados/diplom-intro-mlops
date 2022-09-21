from calculadora.utils import obtener_fracciones


def multiplica(a, b):
    multiplicando = obtener_fracciones(a)
    multiplicador = obtener_fracciones(b)
    return multiplicando * multiplicador
