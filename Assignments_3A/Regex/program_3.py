import re

def main():
    pattern = r'<[^>]+>'
    text = input()
    print (re.findall(pattern, text))

if __name__ == "__main__":
    main()
