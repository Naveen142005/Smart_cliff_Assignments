#6. Group Anagrams


#Reading input
N = int(input())
List = []
for i in range(N): List.append(input().strip() )

dict = {}
for i in List:
    #Sort the strings
    temp = "".join(sorted(i))
    #checking if already present or not
    if temp not in dict:
        dict[temp] = [i] #mapping
    else:
        dict[temp].append(i) #mapping

#Extracting the results
for i in dict.values():
    print(i, end = ', ')