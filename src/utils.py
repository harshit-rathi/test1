"""
Utility functions for testing
"""

def is_even(n: int) -> bool:
    """Check if number is even"""
    return n % 2 == 0


def is_odd(n: int) -> bool:
    """Check if number is odd"""
    return not is_even(n)
