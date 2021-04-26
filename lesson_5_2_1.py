# Assume you have the list xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
#
# Write a loop that prints each of the numbers on a new line.
# Write a loop that prints each number and its square on a new line.
# Write a loop that adds all the numbers from the list into a variable called total.
# You should set the total variable to have the value 0 before you start adding them up,
# and print the value in total after the loop has completed.
# Print the product of all the numbers in the list. (product means all multiplied together)

xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

print("Loop that prints each of the numbers on a new line:")
for x in xs:
    print("Element: " + str(x))

print()  # blank line

print("Loop that prints each number and its square on a new line:")
for x in xs:
    print("Element: " + str(x) + ", Square: " + str(x ** 2))

print()  # blank line

total_value = 0
print("Loop that calculates total:")
for x in xs:
    total_value += x
print("Total: " + str(total_value))

print()  # blank line

print("Loop that calculates a product over the list - option 1 (range):")
product = xs[0]
for i in range(1, len(xs)):
    product *= xs[i]
print("Product calculated by option 1 loop: " + str(product))

print()  # blank line

print("Loop that calculates a product over the list - option 2 (enumerate):")
for index, value in enumerate(xs):
    if index == 0:
        product = value
    elif index == (len(xs) - 1):
        product *= value
        print("Product calculated by option 2 loop: " + str(product))
    else:
        product *= value
