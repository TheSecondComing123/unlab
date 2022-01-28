"""File for helper functions"""


def to_python_index(lst, indexes):
    return f"{lst}{''.join(map(lambda x:'[' + str(x) + ']', indexes))}"
