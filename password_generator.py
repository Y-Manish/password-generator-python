import secrets

LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
SYMBOLS = "!@#$%^&*()_+-=[]{}|;:',.<>?/"


def get_password_length(question: str) -> int:
    """
    Prompt the user for the password length.

    Keeps asking until a positive integer is entered.

    Returns:
        int: The password length.
    """
    while True:
        try:
            password_length = int(input(question))
            if (password_length <= 0):
                print("Enter valid password length")
            else:
                return password_length
        except ValueError:
            print("There is an error, enter an integer")


def ask_yes_no(question: str) -> str:
    """
    Ask the user a yes/no question.

    Returns:
        str: 'y' or 'n'
    """
    while True:
        password_input = input(question).lower()
        if password_input not in ("y", "n"):
            print("Invalid choice!")
        else:
            return password_input


def build_pool(include_lowercase: str,
               include_uppercase: str,
               include_numbers: str,
               include_symbols: str) -> str:
    """
    Build the pool of characters based on the user's choices.

    Returns:
        str: A string containing all allowed characters.
    """
    character_groups = []
    if include_numbers == 'y':
        character_groups.append(NUMBERS)

    if include_symbols == 'y':
        character_groups.append(SYMBOLS)

    if include_lowercase == 'y':
        character_groups.append(LOWERCASE)

    if include_uppercase == 'y':
        character_groups.append(UPPERCASE)

    pool = "".join(character_groups)
    return pool


def add_required_characters(password: str,
                            include_lowercase: str,
                            include_uppercase: str,
                            include_numbers: str,
                            include_symbols: str) -> None:
    if include_lowercase == 'y':
        password.append(secrets.choice(LOWERCASE))
    if include_uppercase == 'y':
        password.append(secrets.choice(UPPERCASE))
    if include_numbers == 'y':
        password.append(secrets.choice(NUMBERS))
    if include_symbols == 'y':
        password.append(secrets.choice(SYMBOLS))


def check_strength(password: str) -> str:
    """
    Evaluate the strength of a password.

    Returns:
        str: Weak, Medium, or Strong.
    """
    score = 0
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any((ch.islower()) for ch in password):
        score += 1
    if any(ch.isupper() for ch in password):
        score += 1
    if any(ch.isdigit() for ch in password):
        score += 1
    if any(ch in SYMBOLS for ch in password):
        score += 1
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


def generate_password() -> str:
    """
    Generate a secure password using the selected options.

    Returns:
        str: The generated password.
    """
    password = []
    while True:
        password_length = get_password_length("Enter password length:")

        include_lowercase = ask_yes_no("Include lowercase letters? (y/n):")
        include_uppercase = ask_yes_no("Include uppercase letters? (y/n):")
        include_numbers = ask_yes_no("Include numbers? (y/n):")
        include_symbols = ask_yes_no("Include symbols? (y/n):")
        pool = build_pool(include_lowercase, include_uppercase,
                          include_numbers, include_symbols)

        required_characters = sum([
            include_lowercase == 'y',
            include_uppercase == 'y',
            include_numbers == 'y',
            include_symbols == 'y'
        ])
        if (pool == ""):
            print("Please select at least one character type.")
        elif required_characters > password_length:
            print("Length and chosen character types do not match. Try again!")
        else:
            break

    add_required_characters(password, include_lowercase,
                            include_uppercase, include_numbers, include_symbols)

    for _ in range(password_length - len(password)):
        password.append(secrets.choice(pool))

    secure_random = secrets.SystemRandom()
    secure_random.shuffle(password)
    return "".join(password)


def main() -> None:
    """
    Run the password generator application.
    """
    while True:
        password = generate_password()
        print("\n" + "=" * 40)
        print("      PASSWORD GENERATOR")
        print("=" * 40)
        print(f"Password : {password}")
        print(f"Strength : {check_strength(password)}")
        print("=" * 40)
        if ask_yes_no("Generate another password? (y/n): ") == 'n':
            print("Exiting...")
            break


if __name__ == "__main__":
    main()
