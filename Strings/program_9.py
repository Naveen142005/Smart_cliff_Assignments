#9. Set Mismatch

#Reading input
N = int(input())
List = list(map(int, input().split()))
List.sort()

for i in range(1 , N):
    if List[i] == List[i - 1]: #Finding the duplicate
        print(List[i], end= ' ')
        break
#Remove duplicate
List = set(List)
#Using natural number sum formula
curr_total = sum(List)
total = (N * (N + 1)) // 2

print(total - curr_total)