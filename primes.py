"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("Enter a number bigger than 0")
    list = [2]
    number = 2
    while len(list) < number_of_primes:
        if number not in list:
            indivisable = True
            for prime in list:
                if number % prime == 0:
                    indivisable = False
            if indivisable:
                list.append(number)
        number += 1
    return list

print(primes(10))