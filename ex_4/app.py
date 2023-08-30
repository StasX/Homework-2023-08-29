import random

numbers = set()

for _ in range(100):
    number = random.randint(1, 1000)
    numbers.add(number)

print(numbers)

total = 0

for number in numbers:
    total += number

count = len(numbers)
average = total/count

print(f"Average of {count} numbers is: {average}")

user_input = input("Please enter a number: ")
number = int(user_input)

msg = "Number exists" if number in numbers else "Numbers doesn't exist"
print(msg)

for number in numbers:
    power = number**2
    print(f"Number: {number}, Power: {power}.")
