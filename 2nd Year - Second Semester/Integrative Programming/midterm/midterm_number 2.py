# Mata, Rhainer Matheuz P.
# BSIT II - 1
# April 6, 2024

total = 0
largest = 0
smallest = 0
total_positive = 0
total_negative = 0
negative_count = 0
between_50_and_100 = 0

print()

for i in range(10):
    number = int(input(f"{i + 1}) Input an integer\t: "))
    total += number

    # initializes the smallest and largest number
    if (i == 0):
        smallest = number
        largest = number

    if (number > largest):
        largest = number
    
    if (number < smallest):
        smallest = number

    if (number > 0):
        total_positive += number

    if (number < 0):
        total_negative += number
        negative_count += 1

    if ((number >= 50) and (number <= 100)):
        between_50_and_100 += 1

print()
print(f"Total\t\t\t\t\t: {total}")
print(f"Largest\t\t\t\t\t: {largest}")
print(f"Smallest\t\t\t\t: {smallest}")
print(f"Total of all positive numbers\t\t: {total_positive}")
print(f"Total of all negative numbers\t\t: {total_negative}")
print(f"Number of negative numbers entered\t: {negative_count}")
print(f"How many between 50 and 100\t\t: {between_50_and_100}")
print()