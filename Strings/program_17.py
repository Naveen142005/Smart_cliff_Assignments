# Remove tuples of length K

input_string = input()
k = int(input())

temp_list = []
flag = False
temp = ""
res = []

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
        if len(temp_list) != k:
            res.append(temp_list)
        temp_list = []

#changing brackets to make it as tuple
res =  (str(res).replace('[','('))
res = res.replace(']' , ')')

#printing the result
print(res)
