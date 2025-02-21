def get_divisors(n):
    """
    This function takes an integer n as input and returns a list of all its divisors.

    Parameters:
    n (int): The integer whose divisors need to be found.

    Returns:
    list: A list containing all divisors of n.
    """
    return [i for i in range(1, n + 1) if n % i == 0]


# Example usage:
print(get_divisors(47))  # Output: [1, 47]
print(get_divisors(28))
print(get_divisors(29))# Output: [1, 2, 4, 7, 14, 28]
a = get_divisors(15)
print(a)
print(len(a))
print(a[-1])
print(a[1:3])
print(sum(a))