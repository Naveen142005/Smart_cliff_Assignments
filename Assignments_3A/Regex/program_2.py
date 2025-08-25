import re

def extract_dates(text):
    return re.findall(r'\d{2}[-/]\d{2}[-/]\d{4}|\d{4}\.\d{2}\.\d{2}', text)

def main():
    text = input("Enter text: ")
    print(extract_dates(text))

if __name__ == "__main__":
    main()
