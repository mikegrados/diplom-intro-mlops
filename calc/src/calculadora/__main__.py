from calculadora import suma, resta
from calculadora.tipo2 import multiplica, division

from calculadora.config import settings


def ejemplo(num_1, num_2):
    res_suma = suma(num_1, num_2)
    print(res_suma)

    res_resta = resta(num_1, num_2)
    print(res_resta)

    res_divide = division(num_1, num_2)
    print(res_divide)

    res_multiplica = multiplica(num_1, num_2)
    print(res_multiplica)


if __name__ == "__main__":
    print(f"Hello {settings['NAME']}")
    ejemplo(settings["NUMBER"], 5)
