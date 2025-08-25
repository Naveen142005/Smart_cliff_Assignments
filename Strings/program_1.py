#1.SEARCH ALPHANUMERIC STRING

string = list(map(str, input().split()))
for i in string:
    #checking alphanumeric string or not
    if not i.isalpha():
        print(i, end = ' ')
