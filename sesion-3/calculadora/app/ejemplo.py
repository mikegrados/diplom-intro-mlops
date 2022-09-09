import operaciones as c


def ejemplo(num_1, num_2):
    res_suma = c.suma(num_1, num_2)
    print(res_suma)

    res_resta = c.resta(num_1, num_2)
    print(res_resta)

    res_divide = c.divide(num_1, num_2)
    print(res_divide)

    res_multiplica = c.multiplica(num_1, num_2)
    print(res_multiplica)


if __name__ == "__main__":
    ejemplo(1, "1/2")
