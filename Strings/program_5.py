#5. Find all numbers Disappeared in a List

#getting input
N = int(input())

#removing duplicates
nums = set(map(int, input().split(',')))

n = len(nums) + 1
nums = set(nums)
res = []
for i in range(1, n):
    #Checking if it is disappeared
    if i not in nums:
        res.append(i)
print(res)