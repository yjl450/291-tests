"""
* In this think-aloud usability test, we will ask you to finish
  a series of tasks, each marked with TODO. Please finish all of them!

* Type checking in Visual Studio Code has been turned on.
  In addition, You can use `mypy tests.py` in the terminal
  to do static type checking. Success in mypy is part of finishing
  the tasks.

* In this test, we use Python 3.11, Documentation: https://docs.python.org/3.11/
  You can also use any kind of resources on the internet,
  except directly asking for answer from AI chatbot.
"""

""" 
Participant: Yihui Wang
Start Time: 14:14
Finish Time:
"""
from typing import Optional
from typing import Callable
from typing_extensions import Literal

# import modules here
from math import sqrt

# Task 1: Simple Types
# Annotate the following variables with correct types

# TODO 1.1 an integer variable
a:int = 12

# TODO 1.2 a string variable
b:str = "hello world"

# TODO 1.3 an array of
c:list[float] = [0, 1.44, -3.14159]

# TODO 1.4
# "one_tuple" is a variable of a tuple with only a single integer
one_tuple:tuple = (1,)
# "int_str_pair" is a variable of a pair (tuple) of one integer and one string
int_str_pair:tuple[int, str] = (12, "hello world")
# "infinite_tuple" is a variable of a tuple, which holds an indefinite number of integer values
infinite_tuple:tuple = (1, 2, 3, 4, 5, 6, 7)

# TODO 1.5 "num_or_none" can be either a number or None,
# so assigning it both types of value is valid

num_or_none: Optional[int] = 12

# when reassigning a value to it, it should not complain
num_or_none = None

# Task 2: Function type signatures
# Add type signature to each function,
# including both argument types and return types


# TODO 2.1 "abs_sqrt" takes an integer and returns a floating point number
def abs_sqrt_(value: int) -> float:
    return sqrt(abs(value))


# TODO 2.2 for the same function
# if the value is smaller than 0, return None
def abs_sqrt(value: int) -> Optional[float]:
    if value >= 0:
        return sqrt(value)
    else:
        return None


# TODO 2.3 "map_num" is similar to the built-in "map" function
# it takes a function and an array of integers
# applies each of the value in the array to the function
# and returns an array of either floating point numbers or None
def map_num(func: Callable[[int], Optional[float]], nums:list[int]) -> list[Optional[float]]:
    # TODO also add type hint for variable "result"
    result: list[Optional[float]] = []
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
        self,
        name: str,
        age: int,
        gender: Literal["Male", "Female"],
        salaries: list[float],
    ) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self.salaries = salaries

    # TODO 2.5 use Record type, write a function
    # argument "new_salaries" can be a single value (such as from user input)
    # or it can be a list of values or None (such as from database query where some months' data are missing)
    # return a list consisting of all the valid salaries (NOT None) from both the record itself and "new_salaries"
    def output_all_salary(self, new_salaries: Optional[float] | list[Optional[float]]) -> list[float]:
        result = []
        for s in self.salaries:
            result.append(s)
        if isinstance(new_salaries, float | int):
            result.append(new_salaries)
        if isinstance(new_salaries, list):
            for s in new_salaries:
                if isinstance(s, float | int):
                    result.append(s)
        return result


# So we can create one record like this
entry: Record = Record("Helen", 12, "Female", [1000.0, 2500.5])

# and we will get the following output
print(entry.output_all_salary([1, 2, None, 3]))  # return [1000.0, 2500.5, 1, 2, 3]
print(entry.output_all_salary([3.14159]))  # return [1000.0, 2500.5, 3.14159]

# If you have finished, run `mypy tests.py` to check for any type errors
# run `python tests.py` to check if the code actually works

a:None | int = 1
