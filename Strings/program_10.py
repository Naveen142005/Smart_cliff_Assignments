#10. Intersection of Two Lists

#reading input
N_1 = int(input())
#converting into a set
List_1 = set(map(int,input().split()))

N_2 = int(input())
List_2 = set(map(int,input().split()))

#Performing intersection operation
print(list(List_1 & List_2))
