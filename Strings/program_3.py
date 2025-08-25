#3)COUNTING THE OCCURRENCE OF AN ELEMENT IN A LIST

#Read the input
num = int(input())
Element_to_count = input()
List = []
for i in range(num):
    temp = input()
    List.append(temp)

#count the number of Element
print(List.count(Element_to_count))