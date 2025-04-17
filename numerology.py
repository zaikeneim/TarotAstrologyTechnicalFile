# numerology.py
import unicodedata

# Pythagorean Numerology Mapping (Case Insensitive)
LETTER_VALUES = {
    'A': 1, 'J': 1, 'S': 1,
    'B': 2, 'K': 2, 'T': 2,
    'C': 3, 'L': 3, 'U': 3,
    'D': 4, 'M': 4, 'V': 4,
    'E': 5, 'N': 5, 'W': 5,
    'F': 6, 'O': 6, 'X': 6,
    'G': 7, 'P': 7, 'Y': 7,
    'H': 8, 'Q': 8, 'Z': 8,
    'I': 9, 'R': 9
}

MASTER_NUMBERS = [11, 22, 33]

def _normalize_text(text):
    """Normalize text: remove accents, convert to uppercase, keep only letters."""
    # Normalize accents (e.g., é -> e)
    nfkd_form = unicodedata.normalize('NFKD', text)
    ascii_text = "".join([c for c in nfkd_form if not unicodedata.combining(c)])
    # Convert to uppercase and filter only letters
    return "".join(filter(str.isalpha, ascii_text.upper()))

def reduce_to_single_digit(number):
    """
    Reduces a number by summing its digits until it's a single digit
    or a master number (11, 22, 33).
    """
    if number in MASTER_NUMBERS:
        return number
    while number > 9:
        number = sum(int(digit) for digit in str(number))
        if number in MASTER_NUMBERS:
            break
    return number

def calculate_numerology(text):
    """
    Calculates the numerology number for a given text string
    using the Pythagorean system.
    """
    cleaned_text = _normalize_text(text)
    if not cleaned_text:
        return 0 # Or handle as appropriate, maybe None or raise error

    total_sum = sum(LETTER_VALUES.get(char, 0) for char in cleaned_text)

    if total_sum == 0:
        return 0 # No letters found

    return reduce_to_single_digit(total_sum)