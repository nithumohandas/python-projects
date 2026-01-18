# Create from a list (duplicates are removed)
import functools
from time import sleep

my_list = [1, 2, 3, 2, 4]
frozen_set = frozenset(my_list)
print(frozen_set)
# Output: frozenset({1, 2, 3, 4})

# Create from a dictionary (only keys are used)
my_dict = {"Website": "Studytonight", "Letters": 12}
frozen_dict_keys = frozenset(my_dict)
print(frozen_dict_keys)
# Output: frozenset({'Website', 'Letters'})

# Create an empty frozenset
empty_frozenset = frozenset()
print(empty_frozenset)
# Output: frozenset()

# Raw strings in python
print(r'C:\Users' + '\\')

class SimpleIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        # Returns the iterator object itself
        return self

    def __next__(self):
        # Returns the next value and updates the state
        if self.current >= self.end:
            raise StopIteration # Signals the end of iteration
        else:
            value = self.current
            self.current += 1
            return value

# Usage
my_iterator = SimpleIterator(1, 4)
for num in my_iterator:
    print(num)


# Python generator with yield

def count_up_to(max_value):
    current = 1
    while current <= max_value:
        yield current
        current += 1

# Using the generator function
counter = count_up_to(5)
for number in counter:
    print(number)


import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    # Schedule both coroutines to run concurrently
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    # Wait for both tasks to complete
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

# Run the top-level coroutine
asyncio.run(main())


try:
    raise ExceptionGroup(
        "Multiple errors occurred",
        [
            NameError("Name not defined"),
            TypeError("Type mismatch"),
            ValueError("Invalid input")
        ]
    )
except* NameError as e:
    print(f"Handling NameError: {e}")
except* TypeError as e:
    print(f"Handling TypeError: {e}")
except* ValueError as e:
    print(f"Handling ValueError: {e}")

async def run_coroutine():
    sleep(1)
    print("in coroutine")


asyncio.run(run_coroutine())

def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args,**kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function_to_decorate(*args)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("No arguments here.")

def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("in decorator")
        result = func(*args, **kwargs)
        print("after decorator")
        return result
    return wrapper

@decorator
def my_method(name):
    print(f"in {name} my_method")

my_method('nithu')

def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print("My arguments are: {0}, {1}".format(arg1,arg2))
        function(arg1, arg2)
    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities I love are {0} and {1}".format(city_one, city_two))

cities("Nairobi", "Accra")