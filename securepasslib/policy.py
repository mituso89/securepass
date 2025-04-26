from dataclasses import dataclass

@dataclass
class PasswordPolicy:
    min_length: int = 8
    min_uppercase: int = 1
    min_lowercase: int = 1
    min_digits: int = 1
    min_special: int = 1