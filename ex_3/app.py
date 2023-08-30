user_input = input("Please enter your salary #1:")
first_salary = int(user_input)
user_input = input("Please enter your salary #2:")
second_salary = int(user_input)
user_input = input("Please enter your salary #3:")
third_salary = int(user_input)
user_input = input("Please enter your salary #4:")
fourth_salary = int(user_input)
user_input = input("Please enter your salary #5:")
fifth_salary = int(user_input)
user_input = input("Please enter your salary #6:")
sixth_salary = int(user_input)

salaries = (fifth_salary, second_salary, third_salary,
            fourth_salary, fifth_salary, sixth_salary)


total = 0

for salary in salaries:
    total += salary

average = total / len(salaries)

print(f"Average of {len(salaries)} salaries is", average)

max_salary = salaries[0]
for salary in salaries:
    if salary > max_salary:
        max_salary = salary
print("Max salary is:", max_salary)

min_salary = salaries[0]
for salary in salaries:
    if salary < min_salary:
        min_salary = salary
print("Min salary is:", min_salary)
