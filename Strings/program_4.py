#4)  LIST ELEMENT EXISTENCE CHECKER

num = int(input())
Element_to_search = input()
List = []
#getting input
for i in range(num):
    temp = input()
    List.append(temp)
#checking if the element present or not
if(List.count(Element_to_search)) != 0:
    print("True")
else:
    print("False")