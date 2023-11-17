"""
Python 3.11 Documentation: https://docs.python.org/3.11/
"""

# import modules here
from math import sqrt
from typing import Callable  # reference
from typing import Literal  # reference

# Task 1: Simple Types
# Annotate the following variables with correct types,
# and assign a valid value to it

# TODO 1.1 an integer variable
a: int = 12

# TODO 1.2 a string variable
b: str = "hello world"

# TODO 1.3 an array of
c: list[float] = [0, 1.44, -3.14159]

# TODO 1.4
# "one_tuple" is a variable of a tuple with only a single integer
one_tuple: tuple[int] = (1,)
# "int_str_pair" is a variable of a pair (tuple) of one integer and one string
int_str_pair: tuple[int, str] = (12, "hello world")
# "infinite_tuple" is a variable of a tuple, which holds an indefinite number of integer values
infinite_tuple: tuple[int, ...] = (1, 2, 3, 4, 5, 6, 7)

# TODO 1.5 "num_or_none" can be either a number or None,
# so assigning it both types of value is valid
num_or_none: int | None = 12
num_or_none = None

# Task 2: Function type signatures
# Add type signature to each function.


# TODO 2.1 "abs_sqrt" takes an integer and returns a floating point number
def abs_sqrt_(value: int) -> float:
    return sqrt(abs(value))


# TODO 2.2 for the same function
# if the value is smaller than 0, return None
def abs_sqrt(value: int) -> float | None:
    if value >= 0:
        return sqrt(value)
    else:
        return None


# TODO 2.3 "map_num" takes an array of integers
# and returns an array of floating point numbers or None
def map_num(func: Callable[[int], float | None], nums: list[int]) -> list[float | None]:
    # TODO also add type hint for variable "result"
    result: list[float | None] = []
    for i in nums:
        result.append(func(i))
    return result


# So that the following is a valid statement
map_result = map_num(abs_sqrt, [1, 2, 3, 4, 5, 6])

# Task 3: create a custom type called "Record"
# Add type signature to each method.
class Record:
    # TODO 2.4 
    # "name" is a string, "age" is an integer,
    # "gender" can only be a value of "Male" or "Female",
    # "salaries" is an array of floating point numbers
    def __init__(
        self, name: str, age: int, gender: Literal["Male", "Female"], salaries: list[float]
    ) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self.salaries = salaries

    # TODO 2.5 use Record type, write a function
    # argument "new_salaries" can be a single value (such as from user input)
    # or it can be a list of values or None (such as from database query where some months' data are missing)
    # return a list consisting of all the salaries from both the record itself and "new_salaries"
    def output_all_salary(self, new_salaries: float | list[float | None]) -> list[float]:
        result:list[float] = self.salaries.copy()
        if isinstance(new_salaries, list):
            for v in new_salaries:
                if v:
                    result.append(v)
        else:
            result.append(new_salaries)
        return result


# So we can create one record like this
entry: Record = Record("Helen", 12, "Female", [1000.0, 2500.5])

# and we will get the following output
print(entry.output_all_salary([1, 2, None, 3]))  # return [1000.0, 2500.5, 1, 2, 3]
print(entry.output_all_salary([3.14159]))  # return [1000.0, 2500.5, 3.14159]
