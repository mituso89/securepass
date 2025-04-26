
import re
from .policy import PasswordPolicy  # 👈 Import from the new file
from .constants.patterns import UPPERCASE_PATTERN, LOWERCASE_PATTERN, DIGIT_PATTERN, SPECIAL_PATTERN


class Validator:
    def __init__(self, policy: PasswordPolicy = PasswordPolicy()):
        self.policy = policy

    def validate(self, password: str) -> list[str]:
        errors = []
        
        if len(password) < self.policy.min_length:
            errors.append(f"Password must be at least {self.policy.min_length} characters.")

        if len(re.findall(r'[A-Z]', password)) < self.policy.min_uppercase:
            errors.append(f"Password must contain at least {self.policy.min_uppercase} uppercase letter(s).")

        if len(re.findall(r'[a-z]', password)) < self.policy.min_lowercase:
            errors.append(f"Password must contain at least {self.policy.min_lowercase} lowercase letter(s).")

        if len(re.findall(r'\d', password)) < self.policy.min_digits:
            errors.append(f"Password must contain at least {self.policy.min_digits} digit(s).")

        if len(re.findall(r'[!@#$%^&*(),.?\":{}|<>]', password)) < self.policy.min_special:
            errors.append(f"Password must contain at least {self.policy.min_special} special character(s).")

        return errors
    def is_strong(self, password: str, min_length: int = 8) -> bool:
        return (
            len(password) >= min_length and
            re.search(UPPERCASE_PATTERN, password) and
            re.search(LOWERCASE_PATTERN, password) and
            re.search(DIGIT_PATTERN, password) and
            re.search(SPECIAL_PATTERN, password)
        )
    
    def strength_score(self, password: str) -> tuple[int, str]:
        score = 0

        if len(password) >= 8:
            score += 1
        if len(password) >= 12:
            score += 1  # bonus for longer passwords
        if re.search(UPPERCASE_PATTERN, password):
            score += 1
        if re.search(LOWERCASE_PATTERN, password):
            score += 1
        if re.search(DIGIT_PATTERN, password):
            score += 1
        if re.search(SPECIAL_PATTERN, password):
            score += 1

        if score <= 2:
            strength = "Very Weak"
        elif score == 3:
            strength = "Weak"
        elif score == 4:
            strength = "Medium"
        elif score == 5:
            strength = "Strong"
        else:
            strength = "Very Strong"

        return score, strength

    def get_password_report(self, password: str) -> dict:
        errors = self.validate(password)
        score, strength = self.strength_score(password)

        return {
            "errors": errors,
            "strength_score": score,
            "strength_text": strength
        }

