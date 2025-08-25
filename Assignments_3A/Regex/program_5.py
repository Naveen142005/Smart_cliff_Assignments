import re

def extract_indian_numbers(text):
    pattern = r'\b(?:\+91[-\s]?|0)?[6-9]\d{9}\b'
    return re.findall(pattern, text)

def main():
    text = input("Enter text:")
    print(extract_indian_numbers(text))

if __name__ == "__main__":
    main()
