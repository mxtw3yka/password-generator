from secrets import *
from math import *
from enum import IntEnum

class Strength(IntEnum):
    Pathetic = 0
    Weak = 30
    Good = 50
    Strong = 70
    Excellent = 120



def create_password(length: int, Characters: str) -> str:
    return ''.join(choice(Characters) for i in range(length))

def get_entropy(length: int, character_number: int) -> float:
    try:
        entropy = length * log2(character_number)
    except ValueError: return 0.0
    return round(entropy, 2)