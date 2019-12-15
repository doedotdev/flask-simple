def add_sub(value_one, value_two):

    data = {
        "value_one": value_one,
        "value_two": value_two,
        "addition": value_one + value_two,
        "subtraction": value_one - value_two,
    }

    return data


def mul_div(value_one, value_two):

    data = {
        "value_one": value_one,
        "value_two": value_two,
        "multiplication": value_one * value_two,
        "division": value_one / value_two,
    }

    return data
