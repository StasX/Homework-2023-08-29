electronics = {100: "Radio", 101: "PC", 102: "TV"}

code = int(input("Please enter a product code: "))
product = input("Please enter a product: ")
electronics[code] = product

code = int(input("Please enter a product code: "))
if code in electronics:
    print(electronics[code])

for key, value in electronics.items():
    print(f"Product ID: {key}, Product Name: {value}.")

code = int(input("Please enter a product code: "))
if code in electronics:
    del electronics[code]

print(electronics)
