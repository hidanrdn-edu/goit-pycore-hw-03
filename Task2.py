# Task 2
import random


def get_numbers_ticket(min, max, quantity): #min > 1, max < 1000 
    if min < 1 or max > 1000 or min >= max or quantity > (max - min + 1):
        return []
    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))
    return sorted(numbers)

print(get_numbers_ticket(1, 100, 5))