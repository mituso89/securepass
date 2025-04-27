# SecurePassLib Documentation 📚

SecurePassLib provides tools to:
- Validate passwords
- Analyze password strength
- Generate random or template-based passwords
- Check passwords against known breaches
- Use a CLI tool for quick access

---

## 📆 Installation

```bash
pip install securepasslib
```

or for development:

```bash
git clone https://github.com/yourusername/securepasslib.git
cd securepasslib
pip install -e .
```

---

## 🧹 Modules Overview

| Module | Purpose |
|:-------|:--------|
| `validator.py` | Validate passwords, calculate entropy, suggest improvements |
| `generator.py` | Generate random or template-based passwords |
| `breach_checker.py` | Check password exposure with HaveIBeenPwned API |
| `cli.py` | Command-line interface for all features |

---

# 🔒 Password Validation

Use a `PasswordPolicy` to define rules and validate passwords.

```python
from securepasslib import PasswordPolicy, Validator

policy = PasswordPolicy(min_length=10, min_uppercase=2)
validator = Validator(policy)

errors = validator.validate("Password123!")
print(errors)
```

---

# 📈 Password Strength Analysis

Get a full password report.

```python
report = validator.get_password_report("Password123!")

print(report)
# {
#   'errors': [],
#   'strength_score': 5,
#   'strength_text': 'Strong',
#   'entropy_bits': 71.54,
#   'suggestions': []
# }
```

---

# 🔑 Password Generation

## Random Secure Password

```python
from securepasslib import PasswordGenerator

gen = PasswordGenerator()
print(gen.generate_random_password(length=16))
```

## Template-Based Password

```python
print(gen.generate_by_template(template_name="strong"))
print(gen.generate_by_template(custom_template="LL-DD-SS", word_length=8))
```

---

# 🛡️ Password Breach Checking

Check if password appeared in public data breaches.

```python
from securepasslib import BreachChecker

if BreachChecker.is_breached("password123"):
    print("⚠️  Password found in breach!")
else:
    print("✅ Password safe.")
```

---

# ⚡ Command Line Interface (CLI)

After installing, you can run directly:

| Command | Purpose |
|:--------|:--------|
| `securepass random` | Generate random password |
| `securepass template` | Generate password using template |
| `securepass analyze` | Analyze password (strength, suggestions) |
| `securepass breach-check` | Check if password has been breached |

### Examples:

```bash
securepass random --length 16
```

```bash
securepass template --custom-template "LL-DD-SS" --word-length 8
```

```bash
securepass analyze
```

```bash
securepass breach-check
```

---

# 🌟 Predefined Security Policies

Use built-in security presets.

```python
from securepasslib import BASIC_POLICY, MEDIUM_POLICY, STRICT_POLICY

validator = Validator(MEDIUM_POLICY)
```

| Policy | Requirements |
|:-------|:-------------|
| BASIC_POLICY | Minimum 8 characters, 1 uppercase, 1 lowercase, 1 digit |
| MEDIUM_POLICY | Minimum 10 characters, includes 1 special character |
| STRICT_POLICY | Minimum 12 characters, 2 uppercase, 2 lowercase, 2 digits, 2 special characters |

---

# 📜 License

MIT License

---

# 🛠 Contribution

Contributions are welcome!

1. Fork this repository.
2. Create a new branch: `git checkout -b my-new-feature`
3. Make your changes and commit: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request.

Please make sure your code passes existing tests.

---

# ❤️ Thank You

Built to help developers create more secure applications easily.
```

