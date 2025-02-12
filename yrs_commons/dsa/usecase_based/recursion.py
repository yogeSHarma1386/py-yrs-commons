# ============= Recursion: Real-World Examples =============
from typing import Dict


def calculate_compound_interest(principal: float, rate: float, years: int) -> float:
    """Real-world example 1: Compound Interest Calculator"""
    if years == 0:
        return principal
    return calculate_compound_interest(principal * (1 + rate), rate, years - 1)


def calculate_directory_size(path_structure: Dict) -> int:
    """Real-world example 2: Directory Size Calculator"""
    total_size = 0
    for item, value in path_structure.items():
        if isinstance(value, dict):
            total_size += calculate_directory_size(value)
        else:
            total_size += value
    return total_size
