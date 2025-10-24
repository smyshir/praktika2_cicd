"""
math_utils.py — вспомогательные математические функции.
Этот модуль демонстрирует работу автодокументации pdoc.
"""

from typing import List

def average(values: List[float]) -> float:
    """
    Вычисляет среднее арифметическое списка чисел.

    Args:
        values (List[float]): список чисел.

    Returns:
        float: среднее значение. Если список пустой — 0.0.
    """
    return sum(values) / len(values) if values else 0.0


def factorial(n: int) -> int:
    """
    Вычисляет факториал числа n рекурсивно.

    Args:
        n (int): целое неотрицательное число.

    Returns:
        int: n! (факториал числа).
    """
    if n < 0:
        raise ValueError("n должно быть неотрицательным")
    return 1 if n in (0, 1) else n * factorial(n - 1)
