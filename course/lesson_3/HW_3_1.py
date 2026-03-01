# 1. Strings:

# Write a function that takes a string and returns its length.


def get_string_length(string: str) -> int:

    return len(string)

    # return: 11


print(get_string_length(string="Hello World"))


# Create a function that takes two strings and returns the concatenated str.


def concatenate_strings(a: str, b: str) -> str:

    return f"{a} {b}"

    # return: Hello World


print(concatenate_strings(a="Hello", b="World"))


# 2. Numbers (Int/float):

# Implement a function that takes a number and returns its square.


def get_number_square(number: int | float) -> int | float:

    return number**2

    # return: 16


print(get_number_square(number=4))


# Create a function that takes two numbers and returns their sum.


def addition(a: int | float, b: int | float) -> int | float:

    return a + b

    # return: 15


print(addition(a=5, b=10))


# Create a function that accepts 2 numbers of type int, performs the division operation, and returns the prime part and the remainder.


def division(a: int, b: int) -> tuple[int, int]:

    return a // b, a % b

    # return: (1, 4)


print(division(a=10, b=6))

# 3. Lists:

# Write a function to calculate the average of a list of numbers.

numbers_list: list[int] = [2, 4, 6, 8, 10]


def calculate_average(list: list) -> float:

    return sum(list) / len(list)

    # return: 6.0


print(calculate_average(list=numbers_list))

# Implement a function that takes two lists and returns a list that contains the common elements of both lists.

fruits: list[str] = ["apple", "banana", "orange", "grape", "mango"]

vegetables: list[str] = ["carrot", "broccoli", "spinach", "pepper", "cucumber"]


def combine_lists(list_1: list, list_2: list) -> list[str]:
    list_1.extend(list_2)
    return list_1

    # return: ['apple', 'banana', 'orange', 'grape', 'mango', 'carrot', 'broccoli', 'spinach', 'pepper', 'cucumber']


print(combine_lists(list_1=fruits, list_2=vegetables))


# 4. Dictionaries:

# Create a function that takes a dictionary and outputs all the keys in that dictionary.

car: dict[str, str | int] = {"brand": "Ford", "model": "Mustang", "year": 1964}


def get_dictionary_keys(dictionary: dict) -> list[str | int]:

    return list(dictionary.keys())

    # return: ['brand', 'model', 'year']


print(get_dictionary_keys(dictionary=car))


# Implement a function that takes two dictionaries and returns a new dictionary that is the union of both dictionaries.

mlb_group_a: dict[str, str] = {
    "Colorado": "Rockies",
    "Chicago": "White Sox",
    "Boston": "Red Sox",
}

mlb_group_b: dict[str, str] = {
    "Minnesota": "Twins",
    "Milwaukee": "Brewers",
    "Seattle": "Mariners",
}


def combine_dictionary(group_a: dict, group_b: dict) -> dict[str, str]:

    return group_a | group_b

    # return: {'Colorado': 'Rockies', 'Chicago': 'White Sox', 'Boston': 'Red Sox', 'Minnesota': 'Twins', 'Milwaukee': 'Brewers', 'Seattle': 'Mariners'}


print(combine_dictionary(group_a=mlb_group_a, group_b=mlb_group_b))

# 5. Sets:

# Write a function that takes two sets and returns their union.

set_a: set[int] = {1, 2, 3}
set_b: set[int] = {4, 5, 6}


def get_union(set1: set, set2: set) -> set[int]:

    return set1.union(set2)

    # return: {1, 2, 3, 4, 5, 6}


print(get_union(set1=set_a, set2=set_b))


# Create a function that checks whether one set is a subset of another.

main_set: set[str] = {"a", "b", "c", '"d'}
set_to_verify: set[str] = {"a", "b", "c"}


def verify_subset(main_set: set, set_to_verify: set) -> None:
    is_subset = set_to_verify.issubset(main_set)
    status = "is" if is_subset else "is not"
    print(f"{set_to_verify} {status} subset of {main_set}: {is_subset}")


verify_subset(main_set=main_set, set_to_verify=set_to_verify)

# 6. Conditional expressions and loops:

# Implement a function that takes a number and outputs "Even" if the number is even, and "Odd" if it is odd.


def verify_number_parity(number: int) -> None:
    result = "is EVEN" if number % 2 == 0 else "is ODD"
    print(f"The number {number} {result}")


verify_number_parity(7)

# Create a function that takes a list of numbers and returns a new list containing only even numbers.

random_number_list: list[int] = [42, 17, 89, 3, 76, 24, 55, 91, 8, 33]


def get_even_number_of_list(number_list: list[int]) -> list[int]:
    return [num for num in number_list if num % 2 == 0]


print(get_even_number_of_list(random_number_list))


# 7. Write a lambda function that determines even/odd.

# The function accepts a parameter (a number) and if it is even, it outputs the word “even”, if not, then “not even”.


parameter: int = lambda number: (
    f"the number {number} is EVEN" if number % 2 == 0 else f"The number {number} is ODD"
)
print(parameter(5))
