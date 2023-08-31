import random

for i in range(1, 15):
    numbers = set()
    while len(numbers) <= 6:
        number = random.randint(1, 37)
        numbers.add(str(number))
    numbers = list(numbers)
    msg = " ".join(numbers)
    print(f"#{i} =>", msg)
