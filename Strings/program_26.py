#26. RESTRICT TUPLES BY FREQUENCY OF FIRST ELEMENT’S VALUE

k = int(input())
input_string = input()


temp_list = []
flag = False
temp = ""
tuples = []

#Parsing the input as tuple
for i in input_string:
    if i.isdigit():
        temp += i
    else:
        if temp != "":
            temp_list.append(temp)
            temp = ""
    if i == ')':
        #not including k length tuples
        tuples.append(temp_list)
        temp_list = []

result = []
dict = dict()

#Extracting tuples
for  tuple_values in tuples:
    #Checking with dict
    if tuple_values[0] not in dict:
        dict[tuple_values[0]] = 1
        result.append(tuple(tuple_values))
    #Check if it is at most k
    elif dict[tuple_values[0]] <= k:
        result.append(tuple(tuple_values))
    #Updating the frequency
    dict[tuple_values[0]] += 1

print(result)


