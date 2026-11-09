"""
Lab 2.2 - Comprehensions and Transformations
"""

NUMBERS = [3, 8, -2, 7, 0, -5, 10]


def squares(numbers: list[int]) -> list[int]:
    return [n ** 2 for n in numbers]


def positives(numbers: list[int]) -> list[int]:
    return [n for n in numbers if n > 0]


def even_squares(numbers: list[int]) -> set[int]:
    return {n ** 2 for n in numbers if n % 2 == 0}


def cubes(numbers: list[int]) -> dict[int, int]:
    return {n: n ** 3 for n in numbers}


if __name__ == "__main__":
    print("Squares:", squares(NUMBERS))
    print("Positives:", positives(NUMBERS))
    print("Even squares:", even_squares(NUMBERS))
    print("Cubes:", cubes(NUMBERS))
