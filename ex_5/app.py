import random

numbers = set()

for i in range(1000):
    number = random.randint(1, 100)
    numbers.add(number)

total = 0
for number in numbers:
    total += number

print(total)
