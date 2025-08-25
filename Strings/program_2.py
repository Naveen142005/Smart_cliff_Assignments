#2. LOWERCASE LETTERS SHOULD COME FIRST

string  = input()
for i in string:
    #checking if the char is lower case or not
    if i.islower():
        print (i, end = '')
for i in string:
    #checking if the char is upper case or not
    if i.isupper():
        print (i, end = '')