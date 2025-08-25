#7)Tuple With Same Product

n = int(input())
nums = [int(input()) for i in range(n)]

mp = {}   # normal dict
ss = len(nums)

# count product frequencies
for i in range(ss):
    for j in range(i + 1, ss):
        prod = nums[i] * nums[j]
        if prod in mp:
            mp[prod] += 1
        else:
            mp[prod] = 1

#calculate result
cnt = 0
for val in mp.values():
    cnt += val * (val - 1) * 4

print(cnt)
