from calculadora.utils import obtener_fracciones


def resta(a, b):
    minuendo = obtener_fracciones(a)
    sustraendo = obtener_fracciones(b)
    return minuendo - sustraendo


if __name__ == "__main__":
    print("HAHA")
