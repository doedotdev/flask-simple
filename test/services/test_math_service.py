from src.services.math import add_sub, mul_div


def test_math_mul_div():

    value_one = 3
    value_two = 4

    result = mul_div(value_one, value_two)

    assert result == {
        "value_one": value_one,
        "value_two": value_two,
        "multiplication": value_one * value_two,
        "division": value_one / value_two,
    }


def test_math_add_sub():

    value_one = 3
    value_two = 4

    result = add_sub(value_one, value_two)

    assert result == {
        "value_one": value_one,
        "value_two": value_two,
        "addition": value_one + value_two,
        "subtraction": value_one - value_two,
    }
