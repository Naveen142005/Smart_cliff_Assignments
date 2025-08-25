import re
def main():
    res = []
    s = list(input().split())
    for i in s:
        if re.search(r'[!@#$%^&*(]', i):
           res.append(i)
    print(res)


if __name__ == "__main__":
    main()
