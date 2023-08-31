import random

numbers = []

for _ in range(20):
    number = random.randint(1, 10)
    numbers.append(number)

counted_numbers = {}

for number in numbers:
    if number in counted_numbers.keys():
        counted_numbers[number] += 1
    else:
        counted_numbers[number] = 1

most_popular_numbers = [(0, 0)]

for item in counted_numbers.items():
    if item[1] > most_popular_numbers[0][1]:
        most_popular_numbers = [item]
    elif item[1] == most_popular_numbers[0][1]:
        most_popular_numbers.append(item)

is_couple_numbers = len(most_popular_numbers) > 1
ends = "s are" if is_couple_numbers else " are "
print(f"Most Popular number{ends}", end=" ")
for item in most_popular_numbers:
    print(item[0], end=", ")
print("\b\b  ")
