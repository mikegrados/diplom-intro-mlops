from operaciones import suma, resta, division, multiplica


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
    ejemplo(1, "1/2")
