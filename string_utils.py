"""
string_utils.py — функции для работы со строками.
"""

def capitalize_words(text: str) -> str:
    """
    Делает первую букву каждого слова заглавной.

    Args:
        text (str): исходная строка.

    Returns:
        str: строка с заглавными первыми буквами.
    """
    return ' '.join(word.capitalize() for word in text.split())


def is_palindrome(text: str) -> bool:
    """
    Проверяет, является ли строка палиндромом.

    Args:
        text (str): исходная строка.

    Returns:
        bool: True, если строка читается одинаково слева направо и справа налево.
    """
    clean = ''.join(ch.lower() for ch in text if ch.isalnum())
    return clean == clean[::-1]
