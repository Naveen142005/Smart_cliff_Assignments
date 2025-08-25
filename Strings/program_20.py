#20. Unique Email Addresses

#reading input
n = int(input())
emails = [input() for i in range(n)]
res = set()

for i in emails:
    local, domain = i.split('@')
    temp = ""
    for j in local:
        if j == '.':
            continue
        #everything ignored after +.
        if j == '+':
            break
        temp += j
    res.add(temp+ '@' +domain)
print(len(res))
