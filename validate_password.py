def validate_password(password):
    if len(password) < 8:
        return False, "Password must have minimum 8 characters."

    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_symbol = False

    for char in password:
        if char.islower():
            has_lowercase = True
        elif char.isupper():
            has_uppercase = True
        elif char.isdigit():
            has_digit = True
        elif char in ['_', '@', '$']:
            has_symbol = True

    if not has_lowercase:
        return False, "Password must contain at least one lowercase letter."
    if not has_uppercase:
        return False, "Password must contain at least one uppercase letter."
    if not has_digit:
        return False, "Password must contain at least one digit."
    if not has_symbol:
        return False, "Password must contain at least one symbol (_/@/$)."

    return True, "Password is safe."


password = input("Enter your password: ")
is_safe, message = validate_password(password)
print(message)
