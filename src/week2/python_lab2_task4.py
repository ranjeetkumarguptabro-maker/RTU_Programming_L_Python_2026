"""
Lab 2.4 - Functional Tools Practice
"""

PRICES = [12.5, 9.9, 15.0, 22.3, 5.0]
QUANTITIES = [2, 5, 1, 3, 4]


def item_totals(prices: list[float], quantities: list[int]) -> list[float]:
    return list(map(lambda p, q: p * q, prices, quantities))


def filter_above(totals: list[float], threshold: float = 30) -> list[float]:
    return list(filter(lambda total: total > threshold, totals))


def pair_up(prices: list[float], quantities: list[int]) -> list[tuple]:
    return list(zip(prices, quantities))


def item_totals_comp(prices: list[float], quantities: list[int]) -> list[float]:
    return [p * q for p, q in zip(prices, quantities)]


def filter_above_comp(totals: list[float], threshold: float = 30) -> list[float]:
    return [total for total in totals if total > threshold]


if __name__ == "__main__":
    totals = item_totals(PRICES, QUANTITIES)

    print("Totals:", totals)
    print("Totals > 30:", filter_above(totals))
    print("Price-quantity pairs:", pair_up(PRICES, QUANTITIES))
    print("Totals (comprehension):", item_totals_comp(PRICES, QUANTITIES))
    print("Totals > 30 (comprehension):", filter_above_comp(totals))

    print("I find list comprehensions easier to read.")
