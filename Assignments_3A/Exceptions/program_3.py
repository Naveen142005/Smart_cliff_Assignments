import re
class InvalidUsernameException(Exception): pass
class InvalidPasswordException(Exception): pass


def validate_username(username):
    if not (6 <= len(username) <= 30):
        raise InvalidUsernameException("The length of the user name should be between 6 and 30 characters.")
    if not re.match(r'^[A-Za-z][A-Za-z0-9_]*$', username):
        raise InvalidUsernameException("Username must start with a letter and contain only letters, digits, or underscores.")


def validate_password(password):
    if len(password) < 8:
        raise InvalidPasswordException("Password must be at least 8 characters long.")
    if not re.search(r'[a-z]', password):
        raise InvalidPasswordException("Password must contain at least one lowercase letter.")
    if not re.search(r'[A-Z]', password):
        raise InvalidPasswordException("Password must contain at least one uppercase letter.")
    if not re.search(r'\d', password):
        raise InvalidPasswordException("Password must contain at least one digit.")
    if not re.search(r'[!@#$%^&*()\-\+.]', password):
        raise InvalidPasswordException("Password must contain at least one special character (!@#$%^&*()-+.)")


def validate_login(username, password):
    validate_username(username)
    validate_password(password)
    print(f"Welcome '{username}'")


def main():
    try:
        uname = input("Enter username:")
        pwd = input("Enter password:")
        validate_login(uname, pwd)
    except(InvalidUsernameException, InvalidPasswordException) as e:
        print("Invalid username or password.")
        print("Reason:", e)


if __name__ == "__main__":
    main()
