# 🔐 Password Generator (Python)

A simple command-line password generator built in Python.

This project generates secure random passwords based on user preferences and evaluates the strength of the generated password.

---

## Features

- Generate passwords of any length
- Choose whether to include:
  - Lowercase letters
  - Uppercase letters
  - Numbers
  - Symbols
- Guarantees that every selected character type appears at least once
- Password strength checker
- Input validation using `try/except`
- Regenerate passwords without restarting the program
- Uses Python's `secrets` module for cryptographically secure random generation

---

## Technologies Used

- Python 3
- secrets module

---

## Project Structure

```
Password-Generator/
│
├── Password_Generator.py
├── README.md
├── .gitignore
└── notes.txt
```

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Y-Manish/password-generator-python.git
```

### 2. Move into the project directory

```bash
cd password-generator-python
```

### 3. Run the program

```bash
python Password_Generator.py
```

---

## Example

```
========================================
      PASSWORD GENERATOR
========================================
Password : 8Q&rbP9!wL
Strength : Strong
========================================
```

---

## Concepts Practiced

This project helped me practice:

- Functions
- Loops
- Input validation
- Exception handling
- String manipulation
- Lists
- Random and secure password generation
- Python type hints
- Docstrings
- Git and GitHub

---

## Learning Goals

This project was built to practice writing clean Python code by using:

- Modular functions
- Meaningful variable names
- Input validation
- Type hints
- Docstrings
- Secure password generation using the `secrets` module
- Git and GitHub version control

## Future Improvements

- Save generated passwords to a file
- Copy password directly to clipboard
- GUI version using Tkinter or CustomTkinter
- Password history
- Custom strength rules
- Unit testing with pytest

---

## Author

**Yarramshetty Manish**

Engineering Student (Robotics & AI)

Learning Python, Data Structures, Algorithms, and Software Development.
