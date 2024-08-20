import re

def check_password_strength(password):
    # Initialize variables
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    # Check for digits
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Password should include at least one number.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Password should include at least one special character.")

    # Determine password strength
    if strength == 5:
        feedback.append("Your password is strong.")
    elif strength >= 3:
        feedback.append("Your password is moderate.")
    else:
        feedback.append("Your password is weak.")

    return feedback

def main():
    print("Password Complexity Checker")
    password = input("Enter a password to check its strength: ")
    result = check_password_strength(password)
    
    for line in result:
        print(line)

if __name__ == "__main__":
    main()