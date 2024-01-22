#!/usr/bin/env python3

def return_evens(integers):
    # List comprehension to filter even numbers
    return [num for num in integers if num % 2 == 0]

# Example usage
print(return_evens([0, 1, 3, 5, 7, 8, 9]))

def make_exclamation(sentences):
    # List comprehension to add exclamation marks
    return [sentence + "!" for sentence in sentences]

# Example usage
print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))

