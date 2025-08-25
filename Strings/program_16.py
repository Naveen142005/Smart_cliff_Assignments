#16. BIDIRECTIONAL TUPLE PAIRS

pairs = eval(input())

count = 0
#finding bidirectional tuple pair's count
for i in range(len(pairs)):
    for j in range(i + 1, len(pairs)):
        if pairs[i] == tuple(reversed(pairs[j])):
            count += 1
print(count)
