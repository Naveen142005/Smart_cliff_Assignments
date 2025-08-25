import random
def main():
    # define the all possible character
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special_chars = "!@#$%&"

    #Combine the all
    all_chars = letters + digits + special_chars
    n = int(input())

    # Generate a random password of length n
    password = "".join(random.choice(all_chars) for _ in range(n))

    print("Generated password:", password)


if __name__ == "__main__":
    main()
