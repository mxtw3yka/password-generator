from enum import Enum
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


class Characters(Enum):
    btn_lower = ascii_lowercase
    btn_upper = ascii_uppercase
    btn_digits = digits
    btn_special = punctuation

character_number = {
    'btn_lower' : len(Characters.btn_lower.value),
    'btn_upper' : len(Characters.btn_upper.value),
    'btn_digits' : len(Characters.btn_digits.value),
    'btn_special' : len(Characters.btn_special.value),
}

generate_password = (
    'btn_refresh','btn_lower','btn_upper','btn_digits','btn_special'
)