#19. 3Sum

n = int(input())
arr = list(map(int , input().split()))
arr.sort()
res = []
for i in range(n):
    #Skipping duplicate values
    if i > 0 and arr[i - 1] == arr[i]:
        continue
    num =  arr[i]
    st = i + 1
    end = n - 1
    #using two sum approach
    while st < end:
        val = num + arr[st] + arr[end]
        if val > 0:
            end -= 1
        elif val < 0:
            st += 1
        else:
            #adding the results
            res.append([arr[st],num, arr[end]])
            # Skipping duplicate values
            while st + 1 < n and arr[st] == arr[st + 1]: st += 1
            while end - 1 >= 0 and arr[end - 1] == arr[end]: end -= 1
            st += 1
            end -= 1
print(res)


