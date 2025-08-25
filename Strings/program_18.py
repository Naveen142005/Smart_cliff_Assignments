#18. POSSIBLE WORDS USING GIVEN CHARACTERS

input_list= list(map(str, input().split(','))) # go, bat, me, eat, goal
charset = list(map(str, input().split(','))) #e, o, b, a, m, g, l

#initializing the dictionary
dict = dict()

#mapping the char from charset
for i in charset:
    dict[i] = True

#Checking if the string can form or not
for string in input_list:
    for char in string:
        if not dict.get(char):
            break
    else:
        print(string, end= ', ')
