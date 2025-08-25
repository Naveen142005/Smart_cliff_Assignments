import re

def same_letter_words(text):
    return re.findall(r'\b([a-zA-Z])[a-zA-Z]*\1\b', text, flags=re.IGNORECASE)

def main():
    text = input("Enter text:")
    print(same_letter_words(text))

if __name__ == "__main__":
    main()
