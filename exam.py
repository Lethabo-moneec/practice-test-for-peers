"""
Python Apprentice Assessment: Core Logic & Algorithms
Focus: Control flow, data manipulation, and problem-solving.
"""

def calculate_shipping_cost(weight, destination):
    """
    Question 1: Conditional Statements
    Calculate shipping based on weight and zone.
    - 'domestic': $5.00 flat rate + $1.50 per lb.
    - 'international': $15.00 flat rate + $5.00 per lb.
    - If weight <= 0, return 0.0.
    """

    if weight <= 0:
        return 0.0
    
    if destination == 'domestic':
        shipping = (weight * 1.50) + 5.00
        return shipping
    elif destination == 'international':
        shipping = (weight * 5.00) + 15.00
        return shipping


def filter_even_numbers(numbers):
    
    even_nums = [num for num in numbers if num % 2 == 0]

    return even_nums

def generate_multiplication_table(n, limit):
    """
    Question 3: Advanced Loops
    Generate a list of strings representing the multiplication table for 'n' 
    up to the 'limit'. 
    Example: n=2, limit=3 -> ["2 * 1 = 2", "2 * 2 = 4", "2 * 3 = 6"]
    """
    multiplication_table = []
    for i in range(1, limit + 1):
        multiplication_table.append(f"{n} * {i} = {n * i}")

    return multiplication_table

def find_longest_word(sentence):
    """
    Question 4: Simple Algorithms
    Find the longest word in a space-separated string.
    - If there is a tie, return the first one found.
    - If the string is empty, return an empty string.
    """
    if sentence == "":
        return ""
    
    words = sentence.split()
    longest_word_length = len(words[0])
    longest_word = words[0]

    for word in words:
        if len(word) == longest_word_length:
            continue
        if len(word) > longest_word_length:
            longest_word_length = len(word)
            longest_word = word
    return longest_word


def fizz_buzz_custom(start, end, fizz_val, buzz_val):
    """
    Question 5: Problem Solving
    Iterate from start to end (inclusive). Return a list where:
    - Multiples of fizz_val are "Fizz"
    - Multiples of buzz_val are "Buzz"
    - Multiples of both are "FizzBuzz"
    - Otherwise, use the number as a string.
    """
    # TODO: Implement logic for custom FizzBuzz range
    pass