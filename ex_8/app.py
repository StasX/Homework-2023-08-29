string = input("Please enter a string: ")

characters = {}

for char in string:
    if char in characters:
        characters[char] += 1
    else:
        characters[char] = 1

if " " in characters:
    del characters[" "]

most_popular = ('', 0)
for item in characters.items():
    if item[1] > most_popular[1]:
        most_popular = item

print(f"Most popular character is {most_popular[0]}")
