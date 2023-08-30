products = ("apple", "banana", "orange", "strawberry", "pineapple",
            "watermelon", "grapes", "mango", "kiwi", "peach")

print(products)

print(products[0])

for product in products:
    print(product*3)

count = 0
for product in products:
    count += len(product)

print(f"Total length of all words is: {count}")
