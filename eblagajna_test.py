from eblagajna import price


def testing_function_price():
    assert price("kis") == 1.50
    return "testing_function_price() passed successfully"


print testing_function_price()
