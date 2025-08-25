#15. REMOVING DUPLICATE ELEMENTS FROM A LIST

N = int(input())
num = [int(input()) for i in range(N)]
# Convert to set to remove duplicates, then back to list
num = list(set(num))
print(num)