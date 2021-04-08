def func(x):
    def res_builder(x):
        if x == 0:
            return 6
        else:
            return 1 / 86 * pow(res_builder(x - 1), 2) - 1 / 52 * res_builder(x - 1)
    return "{:.2e}".format(res_builder(x))


try:
    assert func(2) == "-4.76e-03"
    assert func(13) == "6.35e-22"
except AssertionError:
    print("TEST FAILED")
else:
    print("TEST PASSED")
