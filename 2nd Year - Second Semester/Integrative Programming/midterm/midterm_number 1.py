# Mata, Rhainer Matheuz P.
# BSIT II - 1
# April 6, 2024

def detLargest(param1, param2):
    if (param1 >= param2):
        return param1
    else:
        return param2

def main():
    num1 = int(input("\nInput first integer\t: "))
    num2 = int(input("Input second integer\t: "))
    num3 = int(input("Input third integer\t: "))
    
    largest = detLargest(num1, num2) # returns the largest integer between num1 and num2
    largest = detLargest(largest, num3) # returns the largest integer between the variable "largest" and num3

    print(f"\nLargest integer\t\t: {largest}\n")

main()