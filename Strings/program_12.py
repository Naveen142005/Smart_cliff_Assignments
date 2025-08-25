#12. Formatting of String

string_1 = input()
list = list(map(str,string_1.split()))

print("print String in default order:")
print(string_1)

print("print String in position order:")
print(list[1] , list[0] , list[2])

print("Print string in keywords")
print(list[2] , list[1] , list[0])