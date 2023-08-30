import random

numbers = []

for i in range(100):
    number = random.randint(1, 200)
    numbers.append(number)

print(numbers)

user_input = input("Please enter a number: ")
number = int(user_input)

msg = "number exists" if number in numbers else "number doesn't exist"
print(msg)

user_input = input("Please enter a number: ")
number = int(user_input)

count = 0
for item in numbers:
    if item == number:
        count += 1
print(f"the number found in list {count} times")

user_input = input("Please enter a number: ")
number = int(user_input)

if number in numbers:
    numbers.remove(number)

print(numbers)

another_numbers = []

user_input = input("Please enter a number: ")
number = int(user_input)

for item in numbers:
    if item > number:
        another_numbers.append(item)
print(another_numbers)
