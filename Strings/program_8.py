#8. UNCOMMON WORDS FROM TWO SENTENCES

#Reading the inputs
string_1 = list(input().split())
string_2 = list(input().split())
dict = {}

for i in string_1:
    #checking whether the key there or not
    if i not in dict:
        dict[i] = 1 #Initial mapping
    else: dict[i] += 1

for i in string_2:
    # checking whether the key there or not
    if i not in dict:
        dict[i] = 1 #Initial mapping
    else: dict[i] += 1

for key, values in dict.items():
    if values == 1:
        print(key , end = ' ')
