def calculate_f(n, m):
    f = 25
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            f += (i ** 6) / 13 - (j ** 5)
    f *= 25
    print(f)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            f -= 49 * (i ** 3) + 75 * (i ** 2) + 32
    return "{:.2e}".format(f)


try:
    assert calculate_f(77, 78) == "2.85e+14"
    assert calculate_f(45, 49) == "2.67e+12"
    print("Тест пройден успешно")
except AssertionError:
    print("Ошибка в ожидаемом и полученных значениях")
