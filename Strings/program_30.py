s = input()
n = int(input())
words = [input() for i in range(n)]

word_len = len(words[0])
res = []
end = word_len * n

# Frequency dict for given words
freq = {}
for i in words:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

# checking each starting position in the main string
for i in range(0, len(s)):
    substring = s[i : i + end]
    if len(substring) != end:
        continue

    # make frequency dictionary for the current substring
    curr_fq = {}
    for j in range(0, end, word_len):
        curr_word = substring[j:j + word_len]
        if curr_word in freq:
            if curr_word in curr_fq:
                curr_fq[curr_word] += 1
            else:
                curr_fq[curr_word] = 1
        else:
            break

    #Checking  if both dictionaries match
    if curr_fq == freq:
        res.append(i)

# print all valid starting positions
print(res)
