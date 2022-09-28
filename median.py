"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
numbers.sort()
listlength = len(numbers)
if listlength % 2 == 1:
    median = numbers[listlength//2]
else:
    median = (numbers[listlength//2 - 1] + numbers[listlength//2]) / 2
print(median)
