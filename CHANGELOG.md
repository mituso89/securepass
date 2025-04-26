# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2025-04-26

### Added
- **Password Validation** with customizable `PasswordPolicy`.
- **Password Strength Scoring** (Very Weak → Very Strong).
- **Password Entropy Calculator** (bits of entropy based on character pool).
- **Smart Password Suggestions** for improving weak passwords.
- **Password Generator**:
  - Random secure passwords.
  - Template-based password generation (`L`, `D`, `S`, `W` formats).
  - Custom templates allowed.
- **Password Breach Checking** using HaveIBeenPwned API (k-Anonymity model).
- **CLI Tool**:
  - `random` – Generate random passwords.
  - `template` – Generate passwords from templates.
  - `analyze` – Analyze password strength, entropy, and suggest improvements.
  - `breach-check` – Check if password has appeared in data breaches.
- **Predefined Policy Presets**:
  - `BASIC_POLICY`
  - `MEDIUM_POLICY`
  - `STRICT_POLICY`

### Changed
- Refactored regex patterns and messages into `constants/` folder.
- Improved folder and file structure for modular design.
- Clean error handling with validation exceptions.

---

## [Unreleased]

### Planned
- Policy preset expansion (e.g., NIST standard preset).
- Async breach checking.
- Auto password upgrade suggestions.
- Password reuse detection.
- CLI global installation via `entry_points`.

---

