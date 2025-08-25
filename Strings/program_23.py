#Read input
input_string = list(map(str, input().split(' ')))
length_of_each_element = []

#Find the length of each element
for i in input_string:
    length_of_each_element.append([len(i) , i])

n = len(length_of_each_element)

#Sort by the length
for i in range(n):
    for j in range(i + 1, n):
        if length_of_each_element[i][0] < length_of_each_element[j][0]:
            temp = length_of_each_element[i]
            length_of_each_element[i] = length_of_each_element[j]
            length_of_each_element[j] = temp

result = []
#Extracting Result
for i in length_of_each_element:
    result.append(i[1])

#Print the result
print(result)
