# Write a function to calculate change for a given number (number represents cents) 
# The function will return list, vector or collection of numbers representing the number of 
# quarters(25), dimes(10), nickels (5), pennies (1) that would yield the correct change.
# Example:
# For 83¢, the function will return 3 quarters, 0 dimes, 1 nickel, and 3 pennies.

# Input is cents as integers
# Output is a dictionary of quarters, dimes, nickels and pennies

import math

def calculateChange(cents):
    """Calculates change for a given number of cents

    Parameters
    ----------
    cents : int, required
        cents to be converted to change

    Returns
    ----------
    dictionary: Changes from the given cents

    Raises
    ------
    NotImplementedError
        If no sound is set for the animal or passed in as a
        parameter.
    """
    if type(cents) is not int:
        raise NotImplementedError("This function currently only supports integer inputs")

    coins = {'quarters': 0, 'dimes': 0, 'nickels': 0, 'pennies': 0}

    while cents > 0:
        if cents/25 > 0:
            coins['quarters'] = math.floor(cents/25)
            cents = cents%25
        if cents/10 > 0:
            coins['dimes'] = math.floor(cents/10)
            cents = cents%10
        if cents/5 > 0:
            coins['nickels'] = math.floor(cents/5)
            cents = cents%5
        if cents/1 > 0:
            coins['pennies'] = math.floor(cents/1)
            cents = cents%1
    return coins
    # print(f"{coins['quarters']} quarters, {coins['dimes']} dimes, {coins['nickels']} nickel, and {coins['pennies']} pennies")

print(calculateChange(83))
